# Calculate surface features for the measurement of text complexity:
# Extracted features:
# text length in token
# average sentence length in token
# average characters per word
# average syllables per word
# You can run a demo with: $ python surface_features.py
import spacy
import pyphen
from utils_and_preprocess.utils import safe_division


def get_token(doc):
    """Get token count in a doc without punctuation."""
    return len([tok.text for tok in doc if not tok.is_punct])


def count_syllables(doc):
    """Computes the sum of all syllables per word, using the Pyphen moduls which is
    module to hyphenate text using existing Hunspell hyphenation dictionaries.
    See here https://github.com/Kozea/Pyphen
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    dictionary = pyphen.Pyphen(lang="de_DE")
    return sum([len(dictionary.inserted(token.text).split("-")) for token in doc])


def get_text_length_in_token(doc):
    """Returns the text lenght in token (words).
    :param doc: spacy.tokens.doc.Doc
    :return: int """
    return get_token(doc)


def get_average_sentence_length_in_token(doc):
    """Computes the average sentence lenght in token (words).
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    return safe_division(get_token(doc), len(list(doc.sents)))


def get_average_characters_per_word(doc):
    """Computes the average character per word.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    char = sum([len(tok.text) for tok in doc if not tok.is_punct])
    return safe_division(char, get_token(doc))


def get_average_syllables_per_word(doc):
    """Computes the average syllables per word, using the Pyphen module
    in the function count_syllables.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    return safe_division(count_syllables(doc), get_token(doc))


def demo():
    nlp = spacy.load("de_core_news_sm")
    text = "Das ist meine tolle Banane. " \
           "Die Banane ist reif. " \
           "Sie existiert, um gegessen zu werden. " \
        "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
        "Sie kann gegessen werden, weil sie essbar ist. " \
        "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "

    doc = nlp(text)

    print("### Surface Features ###")
    print("text length in token:", get_text_length_in_token(doc))
    print("sentence length in token:", get_average_sentence_length_in_token(doc))
    print("average number of characters per word:", get_average_characters_per_word(doc))
    print("average number of syllables per word:", get_average_syllables_per_word(doc))

    # output:
    # ### Surface Features ###
    # text length in token: 45
    # sentence length in token: 7.5
    # average number of characters per word: 4.733333333333333
    # average number of syllables per word: 1.9111111111111112


if __name__ == "__main__":
    demo()

