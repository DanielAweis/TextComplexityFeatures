import spacy

from utils_and_preprocess.constants import FEATURES

from features.surface_features import \
    get_average_sentence_length_in_token, \
    get_average_characters_per_word, \
    get_average_syllables_per_word, \
    get_text_length_in_token

from features.syntactic_features import \
    get_average_number_of_noun_phrases_per_sentence, \
    get_average_heights, \
    get_average_number_of_subordinate_clauses_per_sentence, \
    get_average_count_of_sentences_with_verb_as_root, \
    get_average_count_of_sentences_with_nouns_as_root

from features.proportion_of_POS_tags_features import \
    get_POS_tag_proportion_for_verbs, \
    get_POS_tag_proportion_for_aux_verbs, \
    get_POS_tag_proportion_for_nouns, \
    get_POS_tag_proportion_for_adjectives, \
    get_POS_tag_proportion_for_punctuations, \
    get_POS_tag_proportion_for_determiners, \
    get_POS_tag_proportion_for_pronouns, \
    get_POS_tag_proportion_for_conjunctions, \
    get_POS_tag_proportion_for_numerales, \
    get_POS_tag_proportion_for_adpositions

from features.lexical_features import calculate_ttr, \
    calculate_lexical_complexity_score

from features.verb_tense_feature import get_average_number_of_verbs_in_sentence

from features.discourse_features import \
    get_average_count_of_pronouns_per_sentence, \
    get_average_count_of_definite_articles_per_sentence, \
    get_average_count_of_discourse_markers_per_sentence

from features.semantic_similarity_features import \
    get_average_semantic_similarity_of_all_nouns, \
    get_average_semantic_similarity_of_all_verbs, \
    get_average_semantic_similarity_of_all_adjectives


def create_feature_to_idx_dict(features):
    """ Creates a dictionary that maps each feature to its index in the input list
     to keep track of order of elements and for the header for the data frame.
    :param features: A list of features.
    :return: dict
    """
    feature_to_index = dict()
    for i, value in enumerate(features):
        feature = "".join(value)
        feature_to_index[feature] = i

    return feature_to_index


def calculate_features(doc, nlp):
    return [
        # surface features
        get_average_sentence_length_in_token(doc),
        get_average_characters_per_word(doc),
        get_average_syllables_per_word(doc),
        get_text_length_in_token(doc),
        # syntactic features
        get_average_number_of_noun_phrases_per_sentence(doc),
        get_average_heights(doc),
        get_average_number_of_subordinate_clauses_per_sentence(doc),
        get_average_count_of_sentences_with_verb_as_root(doc),
        get_average_count_of_sentences_with_nouns_as_root(doc),
        # POS tag features
        get_POS_tag_proportion_for_verbs(doc),
        get_POS_tag_proportion_for_aux_verbs(doc),
        get_POS_tag_proportion_for_nouns(doc),
        get_POS_tag_proportion_for_adjectives(doc),
        get_POS_tag_proportion_for_punctuations(doc),
        get_POS_tag_proportion_for_determiners(doc),
        get_POS_tag_proportion_for_pronouns(doc),
        get_POS_tag_proportion_for_conjunctions(doc),
        get_POS_tag_proportion_for_numerales(doc),
        get_POS_tag_proportion_for_adpositions(doc),
        # lexical features
        calculate_ttr(doc),
        calculate_lexical_complexity_score(doc),
        # verb tense
        get_average_number_of_verbs_in_sentence(doc),
        # discourse features
        get_average_count_of_pronouns_per_sentence(doc),
        get_average_count_of_definite_articles_per_sentence(doc),
        get_average_count_of_discourse_markers_per_sentence(doc),
        # semantic_similarity_features
        get_average_semantic_similarity_of_all_nouns(doc, nlp),
        get_average_semantic_similarity_of_all_verbs(doc, nlp),
        get_average_semantic_similarity_of_all_adjectives(doc, nlp)
    ]


def demo():
    nlp = spacy.load("de_core_news_md")
    text = "Das ist meine tolle Banane. " \
           "Die Banane ist reif. " \
           "Sie existiert, um gegessen zu werden. " \
           "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
           "Sie kann gegessen werden, weil sie essbar ist. " \
           "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "
    doc = nlp(text)
    vec = calculate_features(doc, nlp)
    feature_to_index = create_feature_to_idx_dict(FEATURES)
    header_features = list(feature_to_index.keys())
    print(header_features)
    print(vec)


if __name__ == "__main__":
    demo()
