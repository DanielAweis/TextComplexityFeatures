# Calculate syntactic features for the measurement of text complexity.
# Extracted features:
# average number of noun phrases per sentence,
# average syntactic tree heights,
# average number of subordinate clauses per sentence,
# average count of sentences with verb as root,
# average count of sentences with nouns as root
# You can run a demo with: $ python syntactic_features.py
import spacy
import statistics
from utils_and_preprocess.utils import safe_division


def get_average_number_of_noun_phrases_per_sentence(doc):
    """ Computes the average number of noun phrases per sentence.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    noun_chunks = [chunk.text for chunk in doc.noun_chunks]
    return safe_division(len(noun_chunks), len(list(doc.sents)))


def get_average_number_of_subordinate_clauses_per_sentence(doc):
    """Computes the average number of subordinate clauses per sentence, based on
    the assumption that in german a subordinate clause is always separated
    by a comma.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    comma_count = sum([sent.text.count(",") for sent in doc.sents])
    return safe_division(comma_count, len(list(doc.sents)))


def tree_height(root):
    """Computes maximum height of sentence's dependency parse tree.
    :param root: spacy.tokens.token.Token
    :return: int """
    if not list(root.children):
        return 1
    else:
        return 1 + max(tree_height(x) for x in root.children)


def get_average_heights(doc):
    """Computes average height of parse trees for each sentence in doc.
    :param doc: spacy.tokens.doc.Doc
    Ex.:
        text = "Das ist eine tolle Banane."
        tree_height = 3
    :return: float """
    roots = [sent.root for sent in doc.sents]
    tree_heights = [tree_height(root) for root in roots]
    return statistics.mean(tree_heights)


def get_average_count_of_sentences_with_verb_as_root(doc):
    """Computes average sentence in doc with a verb as root.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    verb_as_root = [1 for tok in doc if tok.dep_ == "ROOT" and tok.pos_ == "VERB"]
    return safe_division(sum(verb_as_root), len(list(doc.sents)))


def get_average_count_of_sentences_with_nouns_as_root(doc):
    """Computes average sentence in doc with a noun as root.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    noun_as_root = [1 for tok in doc if tok.dep_ == "ROOT" and tok.pos_ == "NOUN"]
    return safe_division(sum(noun_as_root), len(list(doc.sents)))


def demo():
    nlp = spacy.load("de_core_news_sm")
    text = "Das ist meine tolle Banane. " \
           "Die Banane ist reif. " \
           "Sie existiert, um gegessen zu werden. " \
        "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
        "Sie kann gegessen werden, weil sie essbar ist. " \
        "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "

    doc = nlp(text)
    print(text)
    print("### Syntactic Features ###")
    print("Average number per sentences...")
    print("... of noun phrases:", get_average_number_of_noun_phrases_per_sentence(doc))
    print("... of subordinate clauses:", get_average_number_of_subordinate_clauses_per_sentence(doc))
    print("... of syntactic tree heigts:", get_average_heights(doc))
    print("... of verbs as root:", get_average_count_of_sentences_with_verb_as_root(doc))
    print("... of nouns as root:", get_average_count_of_sentences_with_nouns_as_root(doc))

    # output:
    # ### Syntactic Features ###
    # Average number per sentences...
    # ... of noun phrases: 2.3333333333333335
    # ... of subordinate clauses: 0.6666666666666666
    # ... of syntactic tree heigts: 4
    # ... of verbs as root: 0.3333333333333333
    # ... of nouns as root: 0.0


if __name__ == "__main__":
    demo()
