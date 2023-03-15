import spacy
import itertools


def print_similarity(words_list, nlp):

    if not words_list:
        words_list = [
        "apfel banane",
        "fisch aal",
        "mensch kind",
        "sonne kabel",
        "nachts Stadt"
        ]

    for words in words_list:
        tokens = nlp(words)
        for token in tokens:
            # Printing the following attributes of each token.
            # text: the word string, has_vector: if it contains
            # a vector representation in the model,
            # vector_norm: the algebraic norm of the vector,
            # is_oov: if the word is out of vocabulary.
            print(token.text, token.has_vector, token.vector_norm, token.is_oov)
        token1, token2 = tokens[0], tokens[1]
        print(f"Similarity for {token1} and {token2}:", token1.similarity(token2))


def get_all_lemmatized_nouns(doc):
    return [tok.lemma_ for tok in doc if tok.pos_ == "NOUN"]


def create_combinations_of_elements(list_of_lemmas):
    """Create all compinations of elements in sorted order, no repeated elements.
    list_of_lemmas = ['G', 'G', 'A', 'F']
    combinations = [('G', 'G'), ('G', 'A'), ('G', 'F'), ('G', 'A'), ('G', 'F'), ('A', 'F')]
    :param list_of_lemmas: list of strings
    :return: list of strings"""
    combinations = list(itertools.combinations(list_of_lemmas, 2))
    return [' '.join(x) for x in combinations]


def calculate_average_semantic_similarity(list_of_strings, nlp):
    """Compute a semantic similarity estimate. Defaults to cosine over vectors."""
    sem_sim = 0.0
    for words in list_of_strings:
        tokens = nlp(words)
        token1, token2 = tokens[0], tokens[1]
        #print(f"Similarity for {token1} and {token2}:", token1.similarity(token2))
        sem_sim += token1.similarity(token2)

    average_semantic_similarity = sem_sim / len(list_of_strings)
    return average_semantic_similarity


def main():
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

    all_nouns1 = get_all_lemmatized_nouns(doc)
    combinations1 = create_combinations_of_elements(all_nouns1)
    print("average_semantic_similarity for DOC1:", calculate_average_semantic_similarity(combinations1, nlp))

    all_nouns2 = get_all_lemmatized_nouns(doc2)
    combinations2 = set(create_combinations_of_elements(all_nouns2))
    print("average_semantic_similarity for DOC2", calculate_average_semantic_similarity(combinations2, nlp))

    # output:
    # average_semantic_similarity for DOC1: 0.7228063295284907
    # average_semantic_similarity for DOC2 0.1710091012219588


if __name__ == "__main__":
    main()
