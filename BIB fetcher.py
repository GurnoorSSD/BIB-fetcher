import requests
import pyperclip
import re

def clean_clipboard_text(text):
    """Fix common clipboard encoding issues (mojibake)."""
    try:
        return text.encode('latin1').decode('utf-8')
    except UnicodeEncodeError:
        return text

def get_doi_from_title(title):
    """Search for a DOI given an article title using CrossRef API."""
    url = "https://api.crossref.org/works"
    params = {"query.title": title, "rows": 1}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        items = response.json()["message"]["items"]
        if items:
            return items[0]["DOI"]
        else:
            print("❌ No DOI found for the given title.")
    else:
        print("❌ Failed to fetch DOI from CrossRef.")
    return None

def get_bibtex_from_doi(doi):
    """Get BibTeX from DOI."""
    headers = {"Accept": "application/x-bibtex"}
    url = f"https://doi.org/{doi}"
    response = requests.get(url, headers=headers, allow_redirects=True)
    if response.status_code == 200:
        return response.text
    else:
        print(f"❌ Could not retrieve BibTeX (HTTP {response.status_code}).")
        return None

# --------- Main Execution ---------
if __name__ == "__main__":
    raw_text = pyperclip.paste().strip()
    if raw_text:
        cleaned_text = clean_clipboard_text(raw_text)
        
        # Determine if DOI or title
        if cleaned_text.lower().startswith("10."):
            doi = cleaned_text
        else:
            doi = get_doi_from_title(cleaned_text)
            if doi is None:
                exit()
        
        bibtex = get_bibtex_from_doi(doi)
        if bibtex:
            print("\n✅ BibTeX entry:\n")
            print(bibtex)
            pyperclip.copy(bibtex)
            print("\n✔ BibTeX copied to clipboard!")
        else:
            print("❌ Could not retrieve BibTeX.")
    else:
        print("❌ Clipboard is empty. Copy a DOI or article title first.")
