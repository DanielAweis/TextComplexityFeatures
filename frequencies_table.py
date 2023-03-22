# This script generates a json file (token_freq_table.json) with token frequencies
# based on this DeReWo corpus:
# https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/
# And provides a function to read in this list for further work.
import json


def get_frequency_table_from_json_file(json_file_path):
    """Returns frequency table a dict with token as keys and freqs as values.
    :param json_file_path: (str)
    :return: dict """
    with open(json_file_path, "r", encoding="utf-8") as file:
        frequency_tabel = json.load(file)

    return frequency_tabel


def get_token_frequencies_from_corpus(corpus_path):
    """ Returns the frequencies table , which is a dict with token as keys
    and frequencies as values for the DeDrKo corpus.
        ### the corpus looks like this:
            ist	sein	VAFIN	64833211
            im	im	APPRART	62591891
            für	für	APPR	56990511
            des	die	ART	56555049.7224575
    :param corpus_path: str
    :return: dict """
    frequency_table = dict()
    with open(corpus_path, "r", encoding="utf-8") as file:
        for line in file:
            act_line = line.split()
            # the DeReWo corpus is case sensitive so here lowering all tokens
            frequency_table[act_line[0].lower()] = float(act_line[-1])

    return frequency_table


def create_file_with_token_frequencies():
    """Creates a json file in data with the frequency table a
    dict with token as keys and freqs as values.
    :param json_file_path: (str) """
    corpus_path = "data/DeReWo/DeReKo-2014-II-MainArchive-STT.100000.freq"
    data = get_token_frequencies_from_corpus(corpus_path)
    with open("token_freq_table.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    create_file_with_token_frequencies()
