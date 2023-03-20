# type-token-ratio
import spacy


def calculate_ttr(doc):
    """
    Computes the type-token-ratio with lemmatized words.
    :param doc: spacy.tokens.doc.Doc
    :return: float
    """
    lemmatized_words = [tok.lemma_ for tok in doc if not tok.is_punct and not tok.is_space]
    print("lemmatized_words", lemmatized_words)
    unique_words = set(lemmatized_words)
    print("unique_words", unique_words)
    return len(unique_words) / len(lemmatized_words)


def main():
    nlp = spacy.load("de_core_news_sm")
    text = "Die Bananen sind reif. Ich esse gerne eine Banane, weil sie so schön gelb ist. " \
           "Manchmal esse ich auch Gurken, obwohl sie nicht gelb sind."
    doc = nlp(text)
    ttr = calculate_ttr(doc)
    print("Type-Token-Ratio:", ttr)

    # output:
    # lemmatized_words ['der', 'Banane', 'sein', 'reif', 'ich', 'essen', 'gerne', 'ein', 'Banane',
    #   'weil', 'sie', 'so', 'schön', 'gelb', 'sein', 'manchmal', 'essen', 'ich', 'auch', 'Gurke',
    #   'obwohl', 'sie', 'nicht', 'gelb', 'sein']
    # unique_words {'Gurke', 'essen', 'manchmal', 'Banane', 'sein', 'ein', 'weil', 'sie', 'so',
    #   'gelb', 'nicht', 'ich', 'schön', 'obwohl', 'auch', 'gerne', 'reif', 'der'}
    # Type-Token-Ratio: 0.72


if __name__ == "__main__":
    main()

