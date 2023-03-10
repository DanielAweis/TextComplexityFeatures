import spacy
import pyphen
import statistics


# surface features
def get_token(doc):
    """Get token in a doc without punctuation."""
    return [tok.text for tok in doc if not tok.is_punct]


def count_syllables(doc):
    """
    Computes the sum of all syllables per word, using the Pyphen moduls which is
    module to hyphenate text using existing Hunspell hyphenation dictionaries.
    See here https://github.com/Kozea/Pyphen
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    dictionary = pyphen.Pyphen(lang="de_DE")
    return sum([len(dictionary.inserted(token.text).split("-")) for token in doc])


def get_text_length_in_token(doc):
    """
    Computes the text lenght in token (words).
    :param doc: spacy.tokens.doc.Doc
    :return: int
    """
    return len(get_token(doc))


def get_average_sentence_length_in_token(doc):
    """
    Computes the average sentence lenght in token (words).
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    return len(get_token(doc)) / len(list(doc.sents))


def get_average_characters_per_word(doc):
    """
    Computes the average character per word.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    char = sum([len(tok.text) for tok in doc if not tok.is_punct])
    return char / len(get_token(doc))


def get_average_syllables_per_word(doc):
    """
    Computes the average syllables per word, using the Pyphen module
    in the function count_syllables.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    return count_syllables(doc) / len(get_token(doc))


# syntactic features
def get_average_number_of_noun_phrases_per_sentence(doc):
    """
    Computes the average number of noun phrases per sentence.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    return len(noun_chunks) / len(list(doc.sents))


def get_average_number_of_verb_phrases_per_sentence(doc):
    pass


def get_average_number_of_subordinate_clauses_per_sentence(doc):
    """
    Computes the average number of subordinate clauses per sentence, based on
    the assumption that in german a subordinate clause is always separated
    by a comma.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    comma_count = sum([sent.text.count(",") for sent in doc.sents])
    return comma_count / len(list(doc.sents))


def tree_height(root):
    """
    Computes maximum height of sentence's dependency parse tree.
    :param root: spacy.tokens.token.Token
    :return: int
    """
    if not list(root.children):
        return 1
    else:
        return 1 + max(tree_height(x) for x in root.children)


def get_average_heights(doc):
    """
    Computes average height of parse trees for each sentence in doc.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    "Das ist eine tolle Banane. " == tree_height = 3
    """
    roots = [sent.root for sent in doc.sents]
    return statistics.mean([tree_height(root) for root in roots])


# Cohesion features
def get_average_number_of_pronouns_per_sentence(doc):
    """
    Computes average number of pronouns per sentence.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    return sum([1 for token in doc if token.pos_ == "PRON"]) / len(list(doc.sents))


def get_average_number_of_definite_articles_per_sentence(doc):
    """
    Computes average number of definite articles for the sentences in doc, based on
    the assumption that in german the definite articles start with d|D to exclude
    the indefinite articles as they are also tagged with "ART" in spacy.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    def_articles_count = sum([1 for token in doc if token.tag_ == "ART" and token.text.startswith(("d", "D"))])
    return def_articles_count / len(list(doc.sents))


def calculate_all_features(doc):
    return [
        get_average_sentence_length_in_token(doc),
        get_average_characters_per_word(doc),
        get_average_syllables_per_word(doc),
        get_text_length_in_token(doc),
        get_average_number_of_noun_phrases_per_sentence(doc),
        get_average_heights(doc),
        get_average_number_of_subordinate_clauses_per_sentence(doc),
        get_average_number_of_pronouns_per_sentence(doc),
        get_average_number_of_definite_articles_per_sentence(doc)
    ]


def main():
    nlp = spacy.load("de_core_news_sm")
    text = "Das ist meine tolle Banane. " \
           "Die Banane ist reif. " \
           "Sie existiert, um gegessen zu werden. " \
        "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
        "Sie kann gegessen werden, weil sie essbar ist. " \
        "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "
    doc = nlp(text)
    vec = calculate_all_features(doc)
    print(vec)


if __name__ == "__main__":
    main()
