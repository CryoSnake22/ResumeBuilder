from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
TEMPLATE_DIR = BASE_DIR / "templates"
TEX_DIR = BASE_DIR / "tex_outputs"
PDF_DIR = BASE_DIR / "pdf_outputs"
ASSET_DIR = BASE_DIR / "assets"

ASSISTANT_CONT_PATH = BASE_DIR / "private" / "assistant_context.txt"
ASSISTANT_CONTEXT = open(ASSISTANT_CONT_PATH, "r").read()
OPTI_CONT_PATH = BASE_DIR / "private" / "optimization_context.txt"
OPTI_CONTEXT = open(OPTI_CONT_PATH, "r").read()
