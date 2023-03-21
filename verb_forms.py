import spacy


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


def main():
    nlp = spacy.load("de_core_news_sm")
    text = "Die Bananen sind reif. " \
           "Die Gurke war reif." \
           "Der Mann hat Gurkensalat gemacht." \
           "Der Bananensalat wird morgen gemacht werden."
    doc = nlp(text)

    for token in doc:
        # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
        # token.shape_, token.is_alpha, token.is_stop)
        print(token.tag_, token.text, list(token.morph), token.lemma_)

    print(get_verb_forms(doc))
    # [['Pres'], ['Past'], ['Pres', 'Part'], ['Pres', 'Part', 'Inf']]


if __name__ == "__main__":
    main()

