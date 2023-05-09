# Calculates lexical features for the measurement of text complexity.
# Extracted features:
# type-token-ratio
# lexical-complexity-score
# You can run a demo with: $ python lexical_features.py
import spacy
import numpy as np

from utils_and_preprocess.utils import get_data_from_json_file, safe_division
from utils_and_preprocess.constants import TOKEN_FREQ
# based on the DeReWo corpus
tokens_freq = get_data_from_json_file("../"+TOKEN_FREQ)


def calculate_ttr(doc):
    """Computes the type-token-ratio with lemmatized words.
    Ex.:
        doc = "Die Bananen sind reif. Ich esse gerne eine Banane,
                weil sie so schön gelb ist. Manchmal esse ich auch
                Gurken, obwohl sie nicht gelb sind."
        lemmatized_words= ['der', 'Banane', 'sein', 'reif', 'ich', 'essen',
                        'gerne', 'ein', 'Banane', 'weil', 'sie', 'so', 'schön',
                        'gelb', 'sein', 'manchmal', 'essen', 'ich', 'auch',
                        'Gurke', 'obwohl', 'sie', 'nicht', 'gelb', 'sein']
        unique_words= {'Gurke', 'essen', 'manchmal', 'Banane', 'sein', 'ein',
                        'weil', 'sie', 'so', 'gelb', 'nicht', 'ich', 'schön',
                        'obwohl', 'auch', 'gerne', 'reif', 'der'}
        type-token-ratio: 0.72

    :param doc: spacy.tokens.doc.Doc
    :return: float """
    lemmatized_words = [tok.lemma_ for tok in doc if not tok.is_punct and not tok.is_space]
    unique_words = set(lemmatized_words)
    return safe_division(len(unique_words), len(lemmatized_words))


def calculate_lexical_complexity_score(doc):
    """Computes the lexical complexity with lemmatized lowered words as
    proposed from Alva-Manchego et al. (2019):
        ### "The lexical complexity score of a simplified sentence is
        computed by taking the log-ranks of each word in the frequency
        table. The ranks are then aggregated by taking their
        third quartile." ###
    Ex.:
        mock_tokens_freq = {
                    "der": 3,
                    "banane": 2,
                    "sein": 3,
                    "reif": 1
                }
        text = "Die Bananen sind reif."
        tokens = ['der', 'banane', 'sein', 'reif']
        tokens_freq_sentence = {'der': 3, 'banane': 2, 'sein': 3, 'reif': 1}
        log_ranks_sentence = [0.0, 0.6931471805599453, 0.0, 1.3862943611198906]
        third_quartile = 0.8664339756999316
    :param doc: spacy.tokens.doc.Doc
    :param tokens_freq: frequency table (dict: token as keys and freqs as values)
    :return: float """

    # tokenize and lemmatize the doc ignoring punctuation
    tokens = [tok.lemma_.lower() for tok in doc if not tok.is_punct]

    # create a frequency table for the tokens in the doc
    tokens_freq_sentence = {}
    for token in tokens:
        if token in tokens_freq:
            tokens_freq_sentence[token] = tokens_freq[token]

    # calculate the log-ranks of each word in the frequency table
    log_ranks = np.log(np.arange(1, len(tokens_freq) + 1))
    log_ranks_sentence = []
    for token, freq in tokens_freq_sentence.items():
        rank = list(tokens_freq.values()).index(freq) + 1
        log_ranks_sentence.append(log_ranks[rank - 1])

    # calculate the third quartile of the log-ranks
    third_quartile = np.percentile(log_ranks_sentence, 75)

    return third_quartile


def demo():
    nlp = spacy.load("de_core_news_sm")
    text = "Die Bananen sind reif. Ich esse gerne eine Banane, weil sie so schön " \
           "gelb ist. Manchmal esse ich auch Gurken, obwohl sie nicht gelb sind."
    doc = nlp(text)
    print(text)
    ttr = calculate_ttr(doc)
    print("Type-Token-Ratio:", ttr)
    print("Lexical-Complexity-Score:", calculate_lexical_complexity_score(doc))


if __name__ == "__main__":
    demo()

