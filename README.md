#  Bibtex Fetcher from DOI or Title

A Python script that automatically fetches the **BibTeX** entry for a research paper when you provide either:
- Its **DOI**, or
- Its **title** (the script will find the DOI for you).

The script detects automatically whether the clipboard content is a DOI or a title, fetches the BibTeX, **prints it**, and **copies it to your clipboard** for easy pasting into your LaTeX `.bib` file.

---

##  Features
-  **Clipboard-aware** — just copy a DOI or title, then run the script.
-  **Automatic detection** — no need to specify DOI or title; the script figures it out.
-  **CrossRef API integration** — finds the DOI if you only have the title.
-  **DOI.org BibTeX fetch** — gets the BibTeX entry directly from the DOI resolver.
-  **One-step workflow** — fetch, display, and copy to clipboard in one go.

---

## 📦 Requirements

Make sure you have Python 3 installed. Then install the dependencies:

```bash
pip install requests pyperclip
