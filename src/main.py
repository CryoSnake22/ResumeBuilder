from config import DATA_DIR, ASSET_DIR
from load_resume import RenderToLaTeX, compile_pdf
from pdf_preprocessing import parse_pdf


def main():
    # Convert the pdf to text
    # most likely temporary
    input_pdf = input("Please chose a pdf: ")
    pdf_path = ASSET_DIR / f"{input_pdf}.pdf"
    txt_name = f"{input_pdf}.txt"

    parse_pdf(pdf_path, txt_name)

    # We have YAML data and we want to put it to LaTeX
    template_name = "template1.tex"
    data_path = DATA_DIR / "data.yaml"
    tex_path = RenderToLaTeX(data_path, template_name)
    # We want to Render the LaTeX to PDF
    compile_pdf(tex_path)


if __name__ == "__main__":
    main()
