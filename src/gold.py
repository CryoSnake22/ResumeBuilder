from load_resume import RenderToLaTeX, compile_pdf
from config import DATA_DIR, ASSET_DIR

filename = input("input filename")
yaml_path = DATA_DIR / f"{filename}.yaml"
template_name = "template1.tex"
tex_path = RenderToLaTeX(yaml_path, filename, template_name)


# We want to Render the LaTeX to PDF
compile_pdf(tex_path)
