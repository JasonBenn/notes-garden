import re
import shutil
from glob import glob
from typing import List


def prepend_title(contents: List[str]) -> List[str]:
    return contents


def remove_attributes(contents: List[str]) -> List[str]:
    i = 0
    for i, line in enumerate(contents):
        if not re.search("^- \w+:: ", line):
            break
    return contents[i:]


def clean_leading_bullets(contents: List[str]) -> List[str]:
    return [re.sub(r"^    - ", "- ", re.sub(r"^- ", "", x)) for x in contents]


def add_title_metadata(contents: List[str], title: str) -> List[str]:
    metadata = ["---", f"title: {title}", "---", ""]
    return metadata + contents


def clean_links(contents: List[str]) -> List[str]:
    return [re.sub("\[\[pub/(.*)\]\]", "[[\g<1>]]", x) for x in contents]


def flatten(t):
    return [item for sublist in t for item in sublist]


def add_paragraph_spacing(contents: List[str]) -> List[str]:
    return flatten(zip(contents, [''] * (len(contents) - 1)))


def get_title(filepath: str) -> str:
    return filepath.split("/")[-1].rstrip(".md")


def get_filename(title: str) -> str:
    if title == "About these notes":
        return "about"  # Special case for root page: the only place where filename does not match title.
    return title.lower().replace("'", "").replace(" ", "-")


def main():
    # shutil.copytree("/Users/jasonbenn/Downloads/Roam-Export-1613438766737/pub", "staging", dirs_exist_ok=True)
    for filepath in glob("staging/*"):
        contents = open(filepath).read().split("\n")
        contents = remove_attributes(contents)
        contents = clean_leading_bullets(contents)
        contents = clean_links(contents)
        contents = add_paragraph_spacing(contents)
        title = get_title(filepath)
        contents = add_title_metadata(contents, title)
        filename = get_filename(title)
        open(f"content/{filename}.md", "w").write("\n".join(contents))


if __name__ == "__main__":
    main()
