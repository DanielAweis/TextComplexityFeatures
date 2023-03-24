import spacy
from itertools import repeat

from utils import get_data_from_json_file

# TODO: handle this in main script
discourse_markers = get_data_from_json_file("discourse_markers.json")
discourse_markers_with_sense = get_data_from_json_file("discourse_markers_with_sense.json")
all_disc_marker_senses = get_data_from_json_file("all_discourse_marker_senses.json")


# Cohesion features
def get_average_count_of_pronouns_per_sentence(doc):
    """
    Computes average number of pronouns per sentence.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    return sum([1 for token in doc if token.pos_ == "PRON"]) / len(list(doc.sents))


def get_average_count_of_definite_articles_per_sentence(doc):
    """
    Computes average number of definite articles for the sentences in doc, based on
    the assumption that in german the definite articles start with d|D to exclude
    the indefinite articles as they are also tagged with "ART" in spacy.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    def_articles_count = sum([1 for token in doc if token.tag_ == "ART" and token.text.startswith(("d", "D"))])
    return def_articles_count / len(list(doc.sents))


# coherence feature
def get_average_count_of_discourse_markers_per_sentence(doc):
    disc_markers = []

    for token in doc:
        for discourse_marker in discourse_markers:
            if token.text.lower() == discourse_marker.lower():
                disc_markers.append(discourse_marker)

    return len(disc_markers) / len(list(doc.sents))


def find_discourse_markers(doc):
    disc_markers = []

    for token in doc:
        for sense, discourse_marker in discourse_markers_with_sense:
            if token.text.lower() == discourse_marker.lower():
                disc_markers.append((discourse_marker, sense))

    return disc_markers


def get_count_for_discourse_marker_senses(doc):
    dm_from_doc = find_discourse_markers(doc)
    # init empty vec
    counts_vec = list(repeat(0, len(all_disc_marker_senses)))
    for i in range(len(counts_vec)):
        for dm in dm_from_doc:
            if dm[1] == all_disc_marker_senses[i]:
                increate_count = counts_vec[i] + 1
                counts_vec.insert(i+1, increate_count)

    return counts_vec


def demo():
    nlp = spacy.load("de_core_news_sm")
    text = "Das ist meine tolle Banane. " \
           "Die Banane ist reif. " \
           "Sie existiert, um gegessen zu werden, abgesehen davon will ich sie nicht. " \
        "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
        "Sie kann gegessen werden, weil sie essbar ist. " \
        "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "
    doc = nlp(text)

    print("Average count per sentence...")
    print("... of pronouns:", get_average_count_of_pronouns_per_sentence(doc))
    print("... of definite articles:", get_average_count_of_definite_articles_per_sentence(doc))
    print("... of discourse markers:", get_average_count_of_discourse_markers_per_sentence(doc))
    print("Vector with counts of used discourse markers in doc:")
    print(get_count_for_discourse_marker_senses(doc))


    # output
    # Average count per sentence...
    # ... of pronouns: 1.6666666666666667
    # ... of definite articles: 0.16666666666666666
    # ... of discourse markers: 0.5
    # Vector with counts of used discourse markers in doc:
    # [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


if __name__ == "__main__":
    demo()
