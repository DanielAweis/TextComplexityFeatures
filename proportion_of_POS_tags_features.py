# Functions to get the proportion of POS tags per text.
# POS tag counts are normalized by dividing them by the number of tokens per text.
# Number of tokens is defined without punctuations.
import spacy


def get_POS_tag_proportion_for_verbs(doc):
    """Returns the proportion of verbs in the text. Verbs are defined as main
    and aux verbs no matter if its conjugates or in infinitive.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    verb_pos_tags = sum([1 for tok in doc if tok.pos_ in ["VERB", "AUX"]])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return verb_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_aux_verbs(doc):
    """Returns the proportion of verbs in the text.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    verb_pos_tags = sum([1 for tok in doc if tok.pos_ == "AUX"])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return verb_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_nouns(doc):
    """Returns the proportion of nouns in the text.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    noun_pos_tags = sum([1 for tok in doc if tok.pos_ == "NOUN"])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return noun_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_adjectives(doc):
    """Returns the proportion of adjectives and adverbs in the text.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    adj_pos_tags = sum([1 for tok in doc if tok.tag_ in ["ADJD", "ADJA"]])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return adj_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_punctuations(doc):
    """Returns the proportion of punctuations in the text.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    punctuations_pos_tags = sum([1 for tok in doc if tok.pos_ == "PUNCT"])
    num_of_token_in_doc = len(doc)
    return punctuations_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_determiners(doc):
    """Returns the proportion of determiners in the text.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    det_pos_tags = sum([1 for tok in doc if tok.pos_ == "DET"])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return det_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_pronouns(doc):
    """Returns the proportion of pronouns in the text.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    pron_pos_tags = sum([1 for tok in doc if tok.pos_ == "PRON"])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return pron_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_conjunctions(doc):
    """Returns the proportion of subordinating and coordinating conjunction.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    junc_pos_tags = sum([1 for tok in doc if tok.pos_ in ["SCONJ", "CCONJ"]])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return junc_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_numerales(doc):
    """Returns the proportion of numerales or other not alphabetic token.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    num_pos_tags = sum([1 for tok in doc if not tok.is_alpha])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return num_pos_tags / num_of_token_in_doc


def get_POS_tag_proportion_for_adpositions(doc):
    """Returns the proportion of adpositions in the text.
    :param doc: spacy.tokens.doc.Doc
    :return: float """
    adp_pos_tags = sum([1 for tok in doc if tok.pos_ == "ADP"])
    num_of_token_in_doc = sum([1 for tok in doc if not tok.is_punct])
    return adp_pos_tags / num_of_token_in_doc


def demo():
    nlp = spacy.load("de_core_news_md")

    text = "Das ist meine tolle Banane, mit der man gut backen kann. " \
            "Die Banane ist reif. Ich habe viel Geld für die Banane gezahlt." \
            "Sie existiert, um gegessen zu werden. " \
            "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
            "Sie kann gegessen werden, weil sie essbar ist. " \
            "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "

    doc = nlp(text)

    print("Proportion of ...")
    print("... verbs:", get_POS_tag_proportion_for_verbs(doc))
    print("... aux verbs:", get_POS_tag_proportion_for_aux_verbs(doc))
    print("... nouns:", get_POS_tag_proportion_for_nouns(doc))
    print("... adjectives and adverbs:", get_POS_tag_proportion_for_adjectives(doc))
    print("... punctuations:", get_POS_tag_proportion_for_punctuations(doc))
    print("... determiners:", get_POS_tag_proportion_for_determiners(doc))
    print("... pronouns:", get_POS_tag_proportion_for_pronouns(doc))
    print("... junctions:", get_POS_tag_proportion_for_conjunctions(doc))
    print("... numerals and other non alphabetic:", get_POS_tag_proportion_for_numerales(doc))
    print("... adpositions:", get_POS_tag_proportion_for_adpositions(doc))

    # output:
    # Proportion of ...
    # ... verbs: 0.3050847457627119
    # ... aux verbs: 0.1694915254237288
    # ... nouns: 0.13559322033898305
    # ... adjectives and adverbs: 0.1016949152542373
    # ... punctuations: 0.16901408450704225
    # ... determiners: 0.0847457627118644
    # ... pronouns: 0.1864406779661017
    # ... junctions: 0.06779661016949153
    # ... numerals and other non alphabetic: 0.2033898305084746
    # ... adpositions: 0.05084745762711865


if __name__ == "__main__":
    demo()
