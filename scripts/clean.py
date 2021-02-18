import os
import re
import shutil
from glob import glob
from typing import List
import platform


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
    new_contents = []

    def replace_link(match):
        title = match.group(1)
        if not title.startswith("pub/"):
            return "[[" + re.sub("pub/", "", title + ' (not published)') + "]]"
        return "[[" + re.sub("pub/", "", title) + "]]"

    for line in contents:
        new_line = re.sub("\[\[(.*)\]\]", replace_link, line)
        new_contents.append(new_line)
    return new_contents


def flatten(t):
    return [item for sublist in t for item in sublist]


def remove_notes(contents: List[str]) -> List[str]:
    for i, line in enumerate(contents):
        if line == "---":
            break
    return contents[:i]


def add_paragraph_spacing(contents: List[str]) -> List[str]:
    return flatten(zip(contents, [''] * (len(contents))))


def get_title(filepath: str) -> str:
    return re.sub(".md$", "", filepath.split("/")[-1])


def get_filename(title: str) -> str:
    if title == "About these notes":
        return "about"  # Special case for root page: the only place where filename does not match title.
    return title.lower().replace("'", "").replace(" ", "-")


ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ROAM_NOTES_DIR = "/home/flock/roam-notes" if platform.system() == "Linux" else "/Users/jasonbenn/code/roam-notes"


def main():
    notes_path = f"{ROAM_NOTES_DIR}/markdown/pub"
    staging_dirpath = f"{ROOT_DIR}/staging"
    content_dirpath = f"{ROOT_DIR}/content"
    shutil.rmtree(content_dirpath, ignore_errors=True)
    os.mkdir(content_dirpath)
    shutil.rmtree(staging_dirpath, ignore_errors=True)
    shutil.copytree(notes_path, staging_dirpath)
    for filepath in glob(f"{staging_dirpath}/*"):
        contents = open(filepath).read().split("\n")
        contents = remove_attributes(contents)
        contents = clean_leading_bullets(contents)
        contents = clean_links(contents)
        contents = remove_notes(contents)
        contents = add_paragraph_spacing(contents)
        title = get_title(filepath)
        contents = add_title_metadata(contents, title)
        filename = get_filename(title)
        open(f"content/{filename}.md", "w").write("\n".join(contents))


if __name__ == "__main__":
    main()
