import spacy
import itertools


def get_all_lemmatized_nouns(doc):
    """Returns all lemmatized nouns of th text in a list.
    :param doc: spacy.tokens.doc.Doc
    :return: list of strings """
    return [tok.lemma_ for tok in doc if tok.pos_ == "NOUN"]


def get_all_lemmatized_adjectives(doc):
    """Returns all lemmatized adverbs and adjectives of th text in a list.
    :param doc: spacy.tokens.doc.Doc
    :return: list of strings """
    return [tok.lemma_ for tok in doc if tok.tag_ in ["ADJD", "ADJA"]]


def get_all_lemmatized_verbs(doc):
    """Returns all lemmatized verbs of th text in a list.
    :param doc: spacy.tokens.doc.Doc
    :return: list of strings """
    return [tok.lemma_ for tok in doc if tok.pos_ == "VERB"]


def create_combinations_of_elements(list_of_lemmas):
    """Create all compinations of elements in sorted order, no repeated elements.
    list_of_lemmas = ['G', 'G', 'A', 'F']
    combinations = [('G', 'G'), ('G', 'A'), ('G', 'F'), ('G', 'A'), ('G', 'F'), ('A', 'F')]
    :param list_of_lemmas: list of strings
    :return: list of strings """
    combinations = list(itertools.combinations(list_of_lemmas, 2))
    return [' '.join(x) for x in combinations]


def calculate_average_semantic_similarity(list_of_strings, nlp):
    """Compute a semantic similarity estimate. Defaults to cosine over vectors.
    :param list_of_lemmas: list of strings
    :return: float """
    if len(list_of_strings) == 0:
        return 0.0
    sem_sim = 0.0
    for words in list_of_strings:
        tokens = nlp(words)
        token1, token2 = tokens[0], tokens[1]
        #print(f"Similarity for {token1} and {token2}:", token1.similarity(token2))
        if token1.has_vector and token2.has_vector:
            sem_sim += token1.similarity(token2)

    average_semantic_similarity = sem_sim / len(list_of_strings)
    return average_semantic_similarity


def get_average_semantic_similarity_of_all_nouns(doc, nlp):
    all_nouns = get_all_lemmatized_nouns(doc)
    combinations = create_combinations_of_elements(all_nouns)
    return calculate_average_semantic_similarity(combinations, nlp)


def get_average_semantic_similarity_of_all_verbs(doc, nlp):
    all_verbs = get_all_lemmatized_verbs(doc)
    combinations = create_combinations_of_elements(all_verbs)
    return calculate_average_semantic_similarity(combinations, nlp)


def get_average_semantic_similarity_of_all_adjectives(doc, nlp):
    all_adjectives = get_all_lemmatized_adjectives(doc)
    combinations = create_combinations_of_elements(all_adjectives)
    return calculate_average_semantic_similarity(combinations, nlp)


def demo():
    nlp = spacy.load("de_core_news_md")

    text = "Das ist meine tolle Banane. " \
            "Die Banane ist reif. " \
            "Sie existiert, um gegessen zu werden. " \
            "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
            "Sie kann gegessen werden, weil sie essbar ist. " \
            "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "

    text2 = "Das ist meine tolle Banane. " \
           "Der Mann geht ins Kino. " \
           "Sie existiert, um zu schwimmen. " \
           "Je toller eine Politikerin ist, desto mehr möchte sie essen. " \
           "Im Urlaub ist es schön. " \
           "Manchmal gähnt der Fernseher. "

    doc = nlp(text)
    doc2 = nlp(text2)

    print("### average_semantic_similarity for DOC1 ###")
    print("of all nouns:", get_average_semantic_similarity_of_all_nouns(doc, nlp))
    print("of all verbs:", get_average_semantic_similarity_of_all_verbs(doc, nlp))
    print("of all adjectives:", get_average_semantic_similarity_of_all_adjectives(doc, nlp))

    print("### average_semantic_similarity for DOC2 ###")
    print("of all nouns:", get_average_semantic_similarity_of_all_nouns(doc2, nlp))
    print("of all verbs:", get_average_semantic_similarity_of_all_verbs(doc2, nlp))
    print("of all adjectives:", get_average_semantic_similarity_of_all_adjectives(doc2, nlp))

    # output:
    # ### average_semantic_similarity for DOC1 ###
    # of all nouns: 0.7228063295284907
    # of all verbs: 0.2978823661804199
    # of all adjectives: 0.3779828265309334
    # ### average_semantic_similarity for DOC2 ###
    # of all nouns: 0.1710091012219588
    # of all verbs: 0.43449820578098297
    # of all adjectives: 0.8819387356440226


if __name__ == "__main__":
    demo()
