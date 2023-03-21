# type-token-ratio and lexical complexity score
import spacy
import numpy as np
import json


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


def calculate_lexical_complexity_score(doc, tokens_freq):
    """
    Computes the lexical complexity with lemmatized lowered words as
    proposed from Alva-Manchego et al. (2019):
        ### "The lexical complexity score of a simplified sentence is
        computed by taking the log-ranks of each word in the frequency
        table. The ranks are then aggregated by taking their
        third quartile." ###
    :param doc: spacy.tokens.doc.Doc
    :param tokens_freq: frequency table (dict with token as keys and freqs as values)
    :return: float
    """
    # tokenize and lemmatize the doc ignoring punctuation
    tokens = [tok.lemma_.lower() for tok in doc if not tok.is_punct]
    print(tokens)

    # create a frequency table for the tokens in the doc
    tokens_freq_sentence = {}
    for token in tokens:
        if token in tokens_freq:
            tokens_freq_sentence[token] = tokens_freq[token]
    print(tokens_freq_sentence)

    # calculate the log-ranks of each word in the frequency table
    log_ranks = np.log(np.arange(1, len(tokens_freq) + 1))
    print(log_ranks)
    log_ranks_sentence = []
    for token, freq in tokens_freq_sentence.items():
        rank = list(tokens_freq.values()).index(freq) + 1
        log_ranks_sentence.append(log_ranks[rank - 1])
    print(log_ranks_sentence)

    # calculate the third quartile of the log-ranks
    third_quartile = np.percentile(log_ranks_sentence, 75)

    return third_quartile


def get_token_frequencies_from_corpus(corpus_path):
    """
    Returns the frequencies table , which is a dict with token as keys
    and frequencies as values for the DeDrKo corpus.
        ### the corpus looks like this:
            ist	sein	VAFIN	64833211
            im	im	APPRART	62591891
            für	für	APPR	56990511
            des	die	ART	56555049.7224575
    :param corpus_path: str
    :return: dict
    """
    frequency_table = dict()
    with open(corpus_path, "r", encoding="utf-8") as file:
        for line in file:
            act_line = line.split()
            # the DeReWo corpus is case sensitive so here lowering all tokens
            frequency_table[act_line[0].lower()] = float(act_line[-1])

    return frequency_table


def get_frequency_table_from_json_file(json_file_path):
    """Returns frequency table a dict with token as keys and freqs as values.
    :param json_file_path: (str)
    :return: dict """
    with open(json_file_path, "r", encoding="utf-8") as file:
        frequency_tabel = json.load(file)

    return frequency_tabel


def create_file_with_word_frequencies():
    """Creates a json file in data with the frequency table a dict with token as keys and freqs as values.
        # from https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/
    :param json_file_path: (str) """
    corpus_path = "data/DeReWo/DeReKo-2014-II-MainArchive-STT.100000.freq"
    data = get_token_frequencies_from_corpus(corpus_path)
    with open('data/token_freq_table.json', 'w') as f:
        json.dump(data, f)


def demo():
    nlp = spacy.load("de_core_news_sm")
    text = "Die Bananen sind reif. Ich esse gerne eine Banane, weil sie so schön gelb ist. " \
           "Manchmal esse ich auch Gurken, obwohl sie nicht gelb sind."
    #doc = nlp(text)
    #ttr = calculate_ttr(doc)
    #print("Type-Token-Ratio:", ttr)

    # output:
    # lemmatized_words ['der', 'Banane', 'sein', 'reif', 'ich', 'essen', 'gerne', 'ein', 'Banane',
    #   'weil', 'sie', 'so', 'schön', 'gelb', 'sein', 'manchmal', 'essen', 'ich', 'auch', 'Gurke',
    #   'obwohl', 'sie', 'nicht', 'gelb', 'sein']
    # unique_words {'Gurke', 'essen', 'manchmal', 'Banane', 'sein', 'ein', 'weil', 'sie', 'so',
    #   'gelb', 'nicht', 'ich', 'schön', 'obwohl', 'auch', 'gerne', 'reif', 'der'}
    # Type-Token-Ratio: 0.72

    test_tokens_freq = {
        "der": 3,
        "banane": 2,
        "sein": 3,
        "reif": 1
    }

    text2 = "Die Bananen sind reif."
    doc2 = nlp(text2)
    print(calculate_lexical_complexity_score(doc2, test_tokens_freq))
    # ['der', 'banane', 'sein', 'reif']
    # {'der': 3, 'banane': 2, 'sein': 3, 'reif': 1}
    # [0.         0.69314718 1.09861229 1.38629436]
    # [0.0, 0.6931471805599453, 0.0, 1.3862943611198906]
    # 0.8664339756999316

    json_file_path = "data/token_freq_table.json"

    frequency_table = get_frequency_table_from_json_file(json_file_path)
    print(calculate_lexical_complexity_score(doc2, frequency_table))


if __name__ == "__main__":
    # create_file_with_word_frequencies()
    demo()

