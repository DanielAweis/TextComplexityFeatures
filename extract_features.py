import json
import csv
import spacy

from get_features import calculate_all_features


# create a feature to index dict to keep track of order of elements
features = ["average_sentence_length_in_token",
        "average_characters_per_word",
        "average_syllables_per_word",
        "text_length_in_token",
        "average_number_of_noun_phrases_per_sentence",
        "average_heights",
        "average_number_of_subordinate_clauses_per_sentence",
        "average_number_of_pronouns_per_sentence",
        "average_number_of_definite_articles_per_sentence"]
feature_to_index = dict()
for i, value in enumerate(features):
    feature = "".join(value)
    feature_to_index[feature] = i


def get_json_data_from_txt_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data


def get_features_for_all_docs(list_of_dicts, nlp):
    results = dict()
    for elem in list_of_dicts:
        doc = nlp(elem["text"])
        vec = calculate_all_features(doc)
        results[elem["id"]] = vec
    return results


def main():
    miniklexi_file_path = "data/miniklexi_corpus.txt"
    klexikon_file_path = "data/klexi_corpus.txt"
    wiki_file_path = "data/wiki_corpus.txt"

    json_miniklexi = get_json_data_from_txt_file(miniklexi_file_path)
    json_klexikon = get_json_data_from_txt_file(klexikon_file_path)
    json_wiki = get_json_data_from_txt_file(wiki_file_path)

    miniklexi = json_miniklexi["einfache"]  # label 0.0
    klexikon = json_klexikon["klexikon"]  # label 0.5
    wiki = json_wiki["wiki"]  # label 1.0

    small_miniklexi = miniklexi[:5]
    small_klexikon = klexikon[:5]
    small_wiki = wiki[:5]

    nlp = spacy.load("de_core_news_sm")
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


if __name__ == "__main__":
    main()
