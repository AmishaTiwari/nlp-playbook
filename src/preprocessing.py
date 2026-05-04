# preprocessing.py

import re
import contractions
from bs4 import BeautifulSoup

def clean_text(text):
    if not isinstance(text, str):
        return None
        
    # --- HTML CLEANING ---
    # Parse HTML and remove unwanted tags (script/style contain noise like JS/CSS) 
    soup = BeautifulSoup(text, "lxml")
    for tag in soup(["script", "style"]):
        tag.decompose()

    # Tags removed, Content retained with spaces
    text = soup.get_text(separator=" ")

    # --- URL REMOVAL ---
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # --- DECONTRACTION ---
    text = contractions.fix(text)

    # --- WHITESPACE CLEANUP ---
    text = re.sub(r"\s+", " ", text).strip()

    # --- FINAL VALIDATION ---
    if not text:
        return None
        
    return text