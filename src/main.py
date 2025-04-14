from config import DATA_DIR, ASSET_DIR
from load_resume import RenderToLaTeX, compile_pdf
from pdf_preprocessing import parse_pdf
from yaml_processing import generate_yaml, optimize_yaml
from dotenv import load_dotenv
import os

load_dotenv()


def main():
    # Convert the pdf to text
    # most likely temporary
    #
    filename = input("Please chose a pdf: ")
    pdf_path = ASSET_DIR / f"{filename}.pdf"
    txt_path = parse_pdf(pdf_path, filename)
    job_description = None
    # with open(DATA_DIR / "job_description1.txt") as f:
    # job_description = f.read()

    # If there isnt a yaml file yet, you generate one and optimize it

    if not (os.path.isfile(DATA_DIR / f"{filename}.yaml")):
        print("Generating yaml file")
        yaml_path = generate_yaml(txt_path, filename)
        yaml_opti_path = optimize_yaml(yaml_path, filename, job_description)
    # Otherwise use the original ground truth
    else:
        yaml_path = DATA_DIR / f"{filename}.yaml"
        yaml_opti_path = optimize_yaml(yaml_path, filename, job_description)

    # We have YAML data and we want to put it to LaTeX
    template_name = "template1.tex"
    print("Rendering to LateX")
    tex_path = RenderToLaTeX(yaml_opti_path, filename, template_name)

    # We want to Render the LaTeX to PDF
    compile_pdf(tex_path)


if __name__ == "__main__":
    main()
