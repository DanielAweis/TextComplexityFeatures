import spacy
import statistics

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
