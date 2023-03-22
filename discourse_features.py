import spacy

from discourse_markers import get_discourse_markers_from_json_file


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


def demo():
    nlp = spacy.load("de_core_news_sm")
    text = "Das ist meine tolle Banane. " \
           "Die Banane ist reif. " \
           "Sie existiert, um gegessen zu werden, abgesehen davon will ich sie nicht. " \
        "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
        "Sie kann gegessen werden, weil sie essbar ist. " \
        "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "
    doc = nlp(text)
    for sent in doc.sents:
        print(sent)

    discourse_markers = get_discourse_markers_from_json_file("discourse_markers.json")
    print(discourse_markers)

    #for token in doc:
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        # token.shape_, token.is_alpha, token.is_stop)
        #print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              #token.shape_, token.is_alpha, token.is_stop, list(token.morph))


if __name__ == "__main__":
    demo()