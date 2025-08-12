import os
import json
from langchain.tools import tool

@tool
def save_summary(title: str, summary: str) -> str:
    """
    Saves a book summary as JSON to a local file and returns the file path.
    """
    os.makedirs("summaries", exist_ok=True)

    filename = f"{title.replace(' ', '_')}.json"
    filepath = os.path.join("summaries", filename)

    data = {
        "title": title,
        "summary": summary,
        "saved_path": filepath
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return filepath

tools = [save_summary]
