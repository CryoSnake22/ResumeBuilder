import yaml
import subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from config import TEX_DIR, TEMPLATE_DIR, PDF_DIR
from shutil import copy


def RenderToLaTeX(data_path, template_name) -> Path:
    # Set up the Jinja environment with custom delimiters that won't conflict with LaTeX
    tex_output = TEX_DIR / "output.tex"

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        block_start_string="<%",
        block_end_string="%>",
        variable_start_string="<<",
        variable_end_string=">>",
        comment_start_string="<#",
        comment_end_string="#>",
        trim_blocks=True,
        lstrip_blocks=True,
        autoescape=False,
    )

    # Load the template
    template = env.get_template(template_name)

    # Load the YAML data into a dictionary
    with open(data_path, "r") as f:
        data = yaml.safe_load(f)

    # Render the LaTeX template using the YAML data
    print("Rendering YAML to LaTeX")
    rendered_tex = template.render(data)
    print("Rendering Successful")

    # Write the rendered LaTeX to an output file
    print(f"Writing to {tex_output}")
    with open(tex_output, "w") as f:
        f.write(rendered_tex)

    print(f"Successfully generated {tex_output}")
    return tex_output


def compile_pdf(tex_path: Path):
    # This is just me wanting to keep things semi clean in the file system:
    pdf_tex_path = PDF_DIR / tex_path.name
    copy(tex_path, pdf_tex_path)

    result = subprocess.run(
        ["tectonic", pdf_tex_path],
        cwd=PDF_DIR,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("Tectonic error:", result.stderr)
    else:
        print("PDF generated successfully.")
