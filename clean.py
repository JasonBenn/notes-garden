import re
import shutil
from glob import glob
from typing import Dict
from typing import List


def prepend_title(contents: List[str]) -> List[str]:
    return contents


def remove_attributes(contents: List[str]) -> List[str]:
    for i, line in enumerate(contents):
        if not re.search("^- \w+:: ", line):
            break
    return contents[i:]


def clean_leading_bullets(contents: List[str]) -> List[str]:
    return [re.sub(r"^    - ", "- ", re.sub(r"^- ", "", x)) for x in contents]


def add_title_metadata(contents: List[str], title: str) -> List[str]:
    return contents


def update_aliases(contents: List[str], filepaths_by_title: Dict[str, str]) -> List[str]:
    def replace_link(matchobj):
        return '[[' + filepaths_by_title[matchobj.group(1)] + ']]'
    new_contents = []
    for line in contents:
        new_contents.append(re.sub(r"\[\[pub/(.*)\]\]", replace_link, line))
    return new_contents


def get_title(filepath: str) -> str:
    return filepath.split("/")[-1].rstrip(".md")


def get_filename(title: str) -> str:
    return title.lower().replace("'", "").replace(" ", "-")


def main():
    shutil.copytree("/Users/jasonbenn/Downloads/Roam-Export-1613429953018/pub", "staging", dirs_exist_ok=True)
    filepaths_by_title = {}
    for filepath in glob("staging/*"):
        title = get_title(filepath)
        filepaths_by_title[title] = get_filename(title)

    for filepath in glob("staging/Ab*"):
        contents = open(filepath).read().split("\n")
        contents = remove_attributes(contents)
        contents = clean_leading_bullets(contents)
        contents = update_aliases(contents, filepaths_by_title)
        contents = add_title_metadata(contents, title)
        open(f"content/{title}", "w").write(contents.join("\n"))


if __name__ == "__main__":
    main()
