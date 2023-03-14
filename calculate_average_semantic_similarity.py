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


def create_cartesian_product(list_of_lemmas):
    cartesian_product = list(itertools.product(list_of_lemmas, list_of_lemmas))
    return [' '.join(x) for x in cartesian_product]


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

    all_nouns = get_all_lemmatized_nouns(doc)
    cart_prod = set(create_cartesian_product(all_nouns))
    print("average_semantic_similarity for DOC1:", calculate_average_semantic_similarity(cart_prod, nlp))

    all_nouns = get_all_lemmatized_nouns(doc2)
    cart_prod = set(create_cartesian_product(all_nouns))
    print("average_semantic_similarity for DOC2", calculate_average_semantic_similarity(cart_prod, nlp))


if __name__ == "__main__":
    main()
