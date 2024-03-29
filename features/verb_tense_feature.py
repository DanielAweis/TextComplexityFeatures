# Calculate verb tense feature for the measurement of text complexity.
# Extracted features:
# average number of verbs in sentence
# You can run a demo with: $ python verb_tense_features.py
import spacy
from utils_and_preprocess.utils import safe_division


def get_verb_forms(doc):
    """Extracts all verb forms. Returns a list of lists of strings according
    to the sentences verb forms.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    doc_verb_forms = []
    for sent in doc.sents:
        verb_timeforms = []
        for token in sent:
            if token.morph.get("VerbForm"):
                # if VerbForm=Fin get tense
                if token.morph.get("Tense"):
                    verb_form = token.morph.get("Tense")
                # else 'VerbForm=Part' or 'VerbForm=Inf' no tense
                else:
                    verb_form = token.morph.get("VerbForm")

                verb_timeforms.extend(verb_form)
        doc_verb_forms.append(verb_timeforms)
    return doc_verb_forms


def get_average_number_of_verbs_in_sentence(doc):
    """Assuming that more complex tenses with more than two verbs (finite and
    infinite) are difficult to acquire, the average number of all verbs per
    sentence is calculated here.
    Ex.:
        text = "Die Bananen sind reif. " \
           "Die Gurke war reif." \
           "Der Mann hat Gurkensalat gemacht." \
           "Der Bananensalat wird morgen gemacht werden."
        verb_forms = [['Pres'], ['Past'], ['Pres', 'Part'], ['Pres', 'Part', 'Inf']]
        average number of verbs in sentence = 1.75
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    verb_forms = get_verb_forms(doc)
    # make a flat list
    num_of_verbs = len([verb for sent in verb_forms for verb in sent])
    return safe_division(num_of_verbs, len(list(doc.sents)))


def demo():
    nlp = spacy.load("de_core_news_sm")
    text = "Die Bananen sind reif. " \
           "Die Gurke war reif." \
           "Der Mann hat Gurkensalat gemacht." \
           "Der Bananensalat wird morgen gemacht werden."
    doc = nlp(text)

    print(text)
    print("Average number of verbs:", get_average_number_of_verbs_in_sentence(doc))
    # Average number of verbs: 1.75


if __name__ == "__main__":
    demo()

