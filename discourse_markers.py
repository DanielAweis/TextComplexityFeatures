# This script generates a json file (discourse_markers.json) with a list of all
# discourse markers (str) from the DimLex, a lexicon of german discourse markers.
# https://github.com/discourse-lab/dimlex/blob/master/DimLex-documentation.md

from bs4 import BeautifulSoup
from utils import save_to_json_file


def read_DimLex_xml_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    xml_data = BeautifulSoup(data, "xml")

    return xml_data


def get_discours_markers(xml_data):
    entries = xml_data.find_all("entry")
    discourse_markers = [str(entry.get('word')) for entry in entries]

    return discourse_markers


def get_all_relation_senses(xml_data):
    relations = xml_data.find_all("pdtb3_relation")
    all_possible_relations = set([str(entry.get('sense')) for entry in relations])
    return list(all_possible_relations)


def get_discourse_markers_with_sense(xml_data):
    entries = xml_data.find_all("entry")
    discours_marker_with_sense = []

    for entry in entries:
        word = entry.get('word')
        # list with tuples with the senses and their frequencies
        # to sort and get the most frequent
        freq_sense = []
        relations = entry.find_all("pdtb3_relation")
        for rel in relations:
            if rel.get("freq"):
                new_tup = tuple((rel.get("freq"), rel.get("sense")))
                freq_sense.append(new_tup)
            else:
                new_tup = tuple((0.0, rel.get("sense")))
                freq_sense.append(new_tup)
        # sort the tuples based on the float
        # to only get the most frequent marker sense
        most_freq_rel = sorted(freq_sense, key=lambda x: float(x[0]), reverse=True)[0]
        discours_marker_with_sense.append(tuple((most_freq_rel[1], word.lower())))

    return discours_marker_with_sense


def main():
    dimlex_file_path = "data/discourse-lab/dimlex/DimLex.xml"
    xml_data = read_DimLex_xml_file(dimlex_file_path)

    all_relation_senses = get_all_relation_senses(xml_data)
    save_to_json_file(all_relation_senses, "all_discourse_marker_senses.json")

    discourse_markers = get_discours_markers(xml_data)
    save_to_json_file(discourse_markers, "discourse_markers.json")

    discourse_markers_with_sense = get_discourse_markers_with_sense(xml_data)
    save_to_json_file(discourse_markers_with_sense, "discourse_markers_with_sense.json")


if __name__ == "__main__":
    main()


