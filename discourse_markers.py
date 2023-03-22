# This script generates a json file (discourse_markers.json) with a list of all
# discourse markers (str) from the DimLex, a lexicon of german discourse markers.
# And provides a function to read in this list for further work.
# https://github.com/discourse-lab/dimlex/blob/master/DimLex-documentation.md

import json
from bs4 import BeautifulSoup


def get_discourse_markers_from_json_file(json_file_path):
    """Returns discourse markers as a list with strings.
    :param json_file_path: (str)
    :return: dict """
    with open(json_file_path, "r", encoding="utf-8") as file:
        discourse_markers = json.load(file)

    return discourse_markers


def main():
    file_path = "data/discourse-lab/dimlex/DimLex.xml"
    with open(file_path, "r") as f:
        data = f.read()

    xml_data = BeautifulSoup(data, "xml")
    entries = xml_data.find_all("entry")
    discourse_markers = [str(entry.get("word")) for entry in entries]

    with open("discourse_markers.json", "w") as f:
        json.dump(discourse_markers, f)


if __name__ == "__main__":
    main()
