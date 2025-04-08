from pdfminer.high_level import extract_text


class PDFextract:
    def __init__(self):
        pass

    def extract(self, filename):
        return extract_text(filename)


if __name__ == "__main__":
    extract = PDFextract()
    data = extract.extract("charles_resume.pdf")
    with open("charles_output.txt", "w") as f:
        f.write(data)
