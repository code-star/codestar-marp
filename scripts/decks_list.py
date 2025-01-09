import json
import subprocess
import frontmatter
from datetime import datetime
from pathlib import Path
from glob import glob


def count_slides(content):
    return content.count("---\n") - 1


def git_creation_date(path):
    try:
        result = subprocess.run(
            ["git", "log", "--follow", "--format=%aI", "--", str(path)],
            capture_output=True, text=True, check=True
        )
        return result.stdout.strip().splitlines()[-1].split("T")[0]
    except Exception as e:
        print(f"Warning: Unable to get git creation date for {path}: {e}")
        return "1970-01-01"


def process_slides_file(path):
    path = Path(path)

    with path.open("r") as f:
        contents = f.read()
        metadata = frontmatter.loads(contents)

    title = metadata.get("title", "Untitled")
    author = metadata.get("author", "Unknown")
    creation_date = git_creation_date(path)
    total_slides = count_slides(contents)

    deck_path = str(path.parent.relative_to("decks"))

    return {
        "title": title,
        "author": author,
        "path": deck_path,
        "date": creation_date,
        "total_slides": total_slides,
    }


def generate_decks_list():
    slides_files = glob("decks/**/slides.md")

    decks_data = [process_slides_file(file) for file in slides_files]

    with open("decks.json", "w") as f:
        json.dump(decks_data, f, indent=4)

    print(f"Generated decks.json with {len(decks_data)} entries.")


if __name__ == "__main__":
    generate_decks_list()
