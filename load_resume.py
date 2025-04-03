import yaml
from jinja2 import Environment, FileSystemLoader

yaml_file = "data.yaml"  # Input YAML data file
template_dir = "templates"  # Directory containing your LaTeX template
template_file = "template1.tex"  # LaTeX template filename
output_file = "./outputs/output.tex"  # Output LaTeX file

# Set up the Jinja environment with custom delimiters that won't conflict with LaTeX
env = Environment(
    loader=FileSystemLoader("templates/"),
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
template = env.get_template(template_file)

# Load the YAML data into a dictionary
with open(yaml_file, "r") as f:
    data = yaml.safe_load(f)

# Render the LaTeX template using the YAML data
rendered_tex = template.render(data)

# Write the rendered LaTeX to an output file
with open(output_file, "w") as f:
    f.write(rendered_tex)

print(f"Successfully generated {output_file}")
