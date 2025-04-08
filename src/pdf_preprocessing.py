from config import DATA_DIR
from pdfminer.high_level import extract_text


def parse_pdf(pdf_path, filename):
    txt_path = DATA_DIR / f"{filename}.txt"

    text = extract_text(pdf_path)
    with open(txt_path, "w") as f:
        f.write(text)
    return txt_path
