import json
import csv
import spacy

from utils_and_preprocess.constants import MINIKLEXI, KLEXIKON, WIKI

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

# TODO integrate discourse feature
from features.discourse_features import \
    get_average_count_of_pronouns_per_sentence, \
    get_average_count_of_definite_articles_per_sentence, \
    get_average_count_of_discourse_markers_per_sentence

from features.semantic_similarity_features import \
    get_average_semantic_similarity_of_all_nouns, \
    get_average_semantic_similarity_of_all_verbs, \
    get_average_semantic_similarity_of_all_adjectives


# create a feature to index dict to keep track of order of elements
features = [
            # surface features
            "average_sentence_length_in_token",
            "average_characters_per_word",
            "average_syllables_per_word",
            "text_length_in_token",
            # syntactic features
            "average_number_of_noun_phrases_per_sentence",
            "average_heights",
            "average_number_of_subordinate_clauses_per_sentence",
            "average_count_of_sentences_with_verb_as_root",
            "average_count_of_sentences_with_nouns_as_root",
            # POS tag features
            "POS_tag_proportion_for_verbs", 
            "POS_tag_proportion_for_aux_verbs", 
            "POS_tag_proportion_for_nouns", 
            "POS_tag_proportion_for_adjectives", 
            "POS_tag_proportion_for_punctuations", 
            "POS_tag_proportion_for_determiners", 
            "POS_tag_proportion_for_pronouns", 
            "POS_tag_proportion_for_conjunctions", 
            "POS_tag_proportion_for_numerales", 
            "POS_tag_proportion_for_adpositions",
            # lexical features
            "ttr",
            "lexical_complexity_score",
            # verb tense
            "average_number_of_verbs_in_sentence",
            # discourse features
            "average_count_of_pronouns_per_sentence",
            "average_count_of_definite_articles_per_sentence",
            "average_count_of_discourse_markers_per_sentence"
            # semantic_similarity_features
            "average_semantic_similarity_of_all_nouns",
            "average_semantic_similarity_of_all_verbs",
            "average_semantic_similarity_of_all_adjectives"]

feature_to_index = dict()
for i, value in enumerate(features):
    feature = "".join(value)
    feature_to_index[feature] = i


def calculate_all_features(doc, nlp):
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


def get_json_data_from_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


def get_features_for_all_docs(list_of_dicts, nlp):
    results = dict()
    for elem in list_of_dicts:
        doc = nlp(elem["text"])
        vec = calculate_all_features(doc, nlp)
        results[elem["id"]] = vec
    return results


def small_data():
    json_miniklexi = get_json_data_from_txt_file(MINIKLEXI)
    json_klexikon = get_json_data_from_txt_file(KLEXIKON)
    json_wiki = get_json_data_from_txt_file(WIKI)

    miniklexi = json_miniklexi["einfache"]  # label 0.0
    klexikon = json_klexikon["klexikon"]  # label 0.5
    wiki = json_wiki["wiki"]  # label 1.0

    small_miniklexi = miniklexi[:5]
    small_klexikon = klexikon[:5]
    small_wiki = wiki[:5]

    #nlp = spacy.load("de_core_news_sm")
    nlp = spacy.load("de_core_news_md")
    result_small_miniklexi = get_features_for_all_docs(small_miniklexi, nlp)
    result_small_klexikon = get_features_for_all_docs(small_klexikon, nlp)
    result_small_wiki = get_features_for_all_docs(small_wiki, nlp)

    # save results in one csv file
    header = ['#id']
    header_features = list(feature_to_index.keys())
    header.extend(header_features)

    with open("data/small_feature_vectors.csv", "w", encoding="utf-8") as csv_ofile:
        writer = csv.writer(csv_ofile, delimiter=',')
        writer.writerow(i for i in header)
        for key, value in sorted(result_small_miniklexi.items()):
            line = [f"miniklexi_{key}"]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)
        for key, value in sorted(result_small_klexikon.items()):
            line = [f"klexikon_{key}"]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)
        for key, value in sorted(result_small_wiki.items()):
            line = [f"wiki_{key}"]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)


def demo():
    nlp = spacy.load("de_core_news_md")
    text = "Das ist meine tolle Banane. " \
           "Die Banane ist reif. " \
           "Sie existiert, um gegessen zu werden. " \
        "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
        "Sie kann gegessen werden, weil sie essbar ist. " \
        "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "
    doc = nlp(text)
    vec = calculate_all_features(doc, nlp)
    print(vec)


def main():
    json_miniklexi = get_json_data_from_txt_file(MINIKLEXI)
    json_klexikon = get_json_data_from_txt_file(KLEXIKON)
    json_wiki = get_json_data_from_txt_file(WIKI)

    miniklexi = json_miniklexi["einfache"]  # label 0.0
    klexikon = json_klexikon["klexikon"]  # label 0.5
    wiki = json_wiki["wiki"]  # label 1.0

    nlp = spacy.load("de_core_news_md")
    result_small_miniklexi = get_features_for_all_docs(miniklexi, nlp)
    result_small_klexikon = get_features_for_all_docs(klexikon, nlp)
    result_small_wiki = get_features_for_all_docs(wiki, nlp)

    # save results in one csv file
    header = ['#id']
    header_features = list(feature_to_index.keys())
    header.extend(header_features)

    with open("data/feature_vectors.csv", "w", encoding="utf-8") as csv_ofile:
        writer = csv.writer(csv_ofile, delimiter=',')
        writer.writerow(i for i in header)
        for key, value in sorted(result_small_miniklexi.items()):
            line = [f"miniklexi_{key}"]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)
        for key, value in sorted(result_small_klexikon.items()):
            line = [f"klexikon_{key}"]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)
        for key, value in sorted(result_small_wiki.items()):
            line = [f"wiki_{key}"]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)


if __name__ == "__main__":
    # small_data()
    demo()
    # main()
