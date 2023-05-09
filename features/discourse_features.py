# Calculate discourse (cohesion and coherence) features for the measurement
# of text complexity.
# Extracted features:
# average count of pronouns per sentence
# average count of definite articles per sentence
# average count of discourse markers per sentence
# Vector with counts of used discourse markers
# You can run a demo with: $ python discourse_features.py
import spacy
from itertools import repeat

from utils_and_preprocess.utils import get_data_from_json_file, safe_division
from utils_and_preprocess.constants import DISCOURSE_MARKER, \
    DISCOURSE_MARKER_WITH_SENSE, ALL_DISCOURSE_MARKER

discourse_markers = get_data_from_json_file("../" + DISCOURSE_MARKER)
discourse_markers_with_sense = get_data_from_json_file("../" + DISCOURSE_MARKER_WITH_SENSE)
all_disc_marker_senses = get_data_from_json_file("../" + ALL_DISCOURSE_MARKER)


# cohesion features
def get_average_count_of_pronouns_per_sentence(doc):
    """
    Computes average number of pronouns per sentence.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    pronouns = sum([1 for token in doc if token.pos_ == "PRON"])
    return safe_division(pronouns, len(list(doc.sents)))


def get_average_count_of_definite_articles_per_sentence(doc):
    """
    Computes average number of definite articles for the sentences in doc, based on
    the assumption that in german the definite articles start with d|D to exclude
    the indefinite articles as they are also tagged with "ART" in spacy.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    def_articles_count = sum([1 for token in doc if token.tag_ == "ART" and token.text.startswith(("d", "D"))])
    return safe_division(def_articles_count, len(list(doc.sents)))


# coherence feature
def get_average_count_of_discourse_markers_per_sentence(doc):
    """Calculates the average count of discourse markers per sentence.
    Based on the discourse markers from the DimLex, a lexicon of german discourse
    markers.
    For more information see:
    the comment in utils_and_preprocess.discourse_markers.py

    :param doc: spacy.tokens.doc.Doc
    :return: float """
    disc_markers = []

    for token in doc:
        for discourse_marker in discourse_markers:
            if token.text.lower() == discourse_marker.lower():
                disc_markers.append(discourse_marker)

    return safe_division(len(disc_markers), len(list(doc.sents)))


def find_discourse_markers(doc):
    """ Finds the discourse markers in the text based on the DimLex, a lexicon
    of german discourse markers.
    For more information see:
    the comment in utils_and_preprocess.discourse_markers.py

    :param doc: spacy.tokens.doc.Doc
    :return: list of tuples """
    disc_markers = []

    for token in doc:
        for sense, discourse_marker in discourse_markers_with_sense:
            if token.text.lower() == discourse_marker.lower():
                disc_markers.append((discourse_marker, sense))

    return disc_markers


def get_count_for_discourse_marker_senses(doc):
    """Calculates the counts of the discourse markers in the texts and returns
    a list of the counts.

    :param doc: spacy.tokens.doc.Doc
    :return: list of ints """
    dm_from_doc = find_discourse_markers(doc)
    # init empty vec
    counts_vec = list(repeat(0, len(all_disc_marker_senses)))
    for i in range(len(counts_vec)):
        for dm in dm_from_doc:
            if dm[1] == all_disc_marker_senses[i]:
                counts_vec[i] = counts_vec[i] + 1

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

    print(text)
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
    # Vector with counts of used discourse marker senses:
    # [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


if __name__ == "__main__":
    demo()

