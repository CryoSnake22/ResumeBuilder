import yaml
import openai
import re
from config import BASE_DIR, ASSISTANT_CONTEXT, DATA_DIR
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(BASE_DIR / ".env")
client = OpenAI()


def strip_markdown_code_fence(text):
    """
    Remove markdown code fences from the given text.
    This function removes a starting code fence (which may include a language specifier)
    and a trailing code fence, if present.
    """
    # Remove starting fence like "```", "```yaml", etc.
    text = re.sub(r"^```(?:\w+)?\n", "", text)
    # Remove ending fence on its own line (may also follow a newline)
    text = re.sub(r"\n```$", "", text)
    return text.strip()


def escape_latex(text):
    """
    Escapes common LaTeX special characters in the input text.
    """
    # Define a mapping of special characters to their escaped versions.
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "{": r"\{",
        "}": r"\}",
    }
    # Iterate over the mapping and replace each character.
    for char, escaped in replacements.items():
        text = text.replace(char, escaped)
    return text


def generate_yaml(txt_path, filename):
    yaml_path = DATA_DIR / f"{filename}.yaml"

    with open(txt_path, "r") as f:
        resume_text = f.read()

    prompt = ASSISTANT_CONTEXT + resume_text

    response = client.responses.create(model="gpt-4o", input=prompt)

    output_text = response.output_text
    output_text = strip_markdown_code_fence(output_text)
    output_text = escape_latex(output_text)

    with open(yaml_path, "w") as f:
        f.write(output_text)
    return yaml_path
