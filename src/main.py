from config import BASE_DIR, DATA_DIR, ASSET_DIR
from load_resume import RenderToLaTeX, compile_pdf
from pdf_preprocessing import parse_pdf
from yaml_processing import generate_yaml
from dotenv import load_dotenv

load_dotenv()


def main():
    # Convert the pdf to text
    # most likely temporary
    filename = input("Please chose a pdf: ")

    pdf_path = ASSET_DIR / f"{filename}.pdf"

    txt_path = parse_pdf(pdf_path, filename)

    # yaml_path = generate_yaml(txt_path, filename)
    # debugging:
    yaml_path = DATA_DIR / "bhavna_resume.yaml"

    # We have YAML data and we want to put it to LaTeX

    template_name = "template1.tex"
    tex_path = RenderToLaTeX(yaml_path, filename, template_name)

    # We want to Render the LaTeX to PDF
    compile_pdf(tex_path)


if __name__ == "__main__":
    main()
