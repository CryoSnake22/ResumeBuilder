from pdfminer.high_level import extract_text


class PDFextract:
    def __init__(self):
        pass

    def extract(self, filename):
        return extract_text(filename)
