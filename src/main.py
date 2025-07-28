from config import DATA_DIR, ASSET_DIR
from load_resume import RenderToLaTeX, compile_pdf
from pdf_preprocessing import parse_pdf
from yaml_processing import generate_yaml, optimize_yaml
from dotenv import load_dotenv
import os

load_dotenv()


def choose_resume_name():
    resumes = [f for f in ASSET_DIR.glob("*.pdf")]
    if not resumes:
        print("No resumes found in asset directory.")
        exit()

    print("Select a resume:")
    for i, resume in enumerate(resumes, start=1):
        print(f"{i}. {resume.stem}")  # just name, no .pdf

    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(resumes):
                return resumes[choice - 1].stem  # returns name only
            else:
                print(f"Please enter a number between 1 and {len(resumes)}")
        except ValueError:
            print("Invalid input, please enter a number.")


# Usage example:

# Usage example:


def main():
    # Convert the pdf to text
    # most likely temporary
    #

    filename = choose_resume_name()
    print(f"You selected: {filename}")
    # filename = input("Please chose a pdf: ")
    user_prompt = input("Any instructions ? \n")
    "os.times_result"
    pdf_path = ASSET_DIR / f"{filename}.pdf"
    print("Parsing PDF...\n")
    txt_path = parse_pdf(pdf_path, filename)
    print("PDF parsed\n")
    job_description = None
    # with open(DATA_DIR / "job_description1.txt") as f:
    # job_description = f.read()

    # If there isnt a yaml file yet, you generate one and optimize it

    if not (os.path.isfile(DATA_DIR / f"{filename}.yaml")):
        print("Generating yaml file")
        yaml_path = generate_yaml(txt_path, filename)
        yaml_opti_path = optimize_yaml(
            yaml_path, filename, job_description, user_prompt
        )
    # Otherwise use the original ground truth
    else:
        print("Found Ground Truth Resume")
        yaml_path = DATA_DIR / f"{filename}.yaml"
        yaml_opti_path = optimize_yaml(
            yaml_path, filename, job_description, user_prompt
        )

    # We have YAML data and we want to put it to LaTeX
    template_name = "template1.tex"
    print("Rendering to LateX")
    tex_path = RenderToLaTeX(yaml_opti_path, filename, template_name)

    # We want to Render the LaTeX to PDF
    print("Compiling to PDF\n")
    compile_pdf(tex_path)
    print("Job Complete!\n")


if __name__ == "__main__":
    main()
