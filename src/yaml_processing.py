import yaml
import openai
from config import BASE_DIR
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(BASE_DIR / ".env")
client = OpenAI()


def generate_yaml(txt_path):
    with open(txt_path, "r") as f:
        text = f.read()
    response = client.responses.create(
        model="gpt-4o", input="Write a one-sentence bedtime story about a unicorn."
    )
    print(response.output_text)
