# The script extracts the text complexity features for the lexica-corpus, which
# contains of text from three Wiki-based lexica in german language representing
# three different levels of text complexity.
# For more information on the lexica-corpus see:
# https://github.com/fhewett/lexica-corpus
# You can run the demo in the commandline:
# $ python extract_features_lexica_corpus.py -d True
# If you want to run the script with the complete lexica-corpus make sure that
# you have the data stored like in the constants.py declared
import csv
import spacy
import click

from extract_features import calculate_features, create_feature_to_idx_dict

from constants import MINIKLEXI, KLEXIKON, WIKI, FEATURES, \
    DEMO_MINIKLEXI, DEMO_KLEXIKON, DEMO_WIKI
from utils_and_preprocess.utils import get_data_from_json_file


def get_features_for_lexica_corpus(list_of_dicts, nlp):
    results = dict()
    for elem in list_of_dicts:
        doc = nlp(elem["text"])
        vec = calculate_features(doc, nlp)
        results[elem["id"]] = vec
    return results


def play_demo():
    json_miniklexi = get_data_from_json_file(DEMO_MINIKLEXI)
    json_klexikon = get_data_from_json_file(DEMO_KLEXIKON)
    json_wiki = get_data_from_json_file(DEMO_WIKI)

    demo_miniklexi = json_miniklexi["einfache"]  # label 0.0
    demo_klexikon = json_klexikon["klexikon"]  # label 0.5
    demo_wiki = json_wiki["wiki"]  # label 1.0

    nlp = spacy.load("de_core_news_md")

    result_small_miniklexi = get_features_for_lexica_corpus(demo_miniklexi, nlp)
    result_small_klexikon = get_features_for_lexica_corpus(demo_klexikon, nlp)
    result_small_wiki = get_features_for_lexica_corpus(demo_wiki, nlp)

    # create a feature to index dict to keep track of order of elements
    feature_to_index = create_feature_to_idx_dict(FEATURES)

    # save results in one csv file
    header = ["#id", "#label"]
    header_features = list(feature_to_index.keys())
    header.extend(header_features)

    with open("demo_data/demo_result.csv", "w", encoding="utf-8") as csv_ofile:
        writer = csv.writer(csv_ofile, delimiter=',')
        writer.writerow(i for i in header)
        for key, value in sorted(result_small_miniklexi.items()):
            line = [f"miniklexi_{key}", 0.0]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)
        for key, value in sorted(result_small_klexikon.items()):
            line = [f"klexikon_{key}", 0.5]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)
        for key, value in sorted(result_small_wiki.items()):
            line = [f"wiki_{key}", 1.0]
            vecs = [round(i, 6) for i in value]
            line.extend(vecs)
            writer.writerow(line)

    print("Find the extracted demo results in demo_data/demo_result.csv")


@click.command()
@click.option("-d", "demo", type=bool, default=True, help="If you want to see a small demo.")
def cli(demo):
    if demo:
        play_demo()
    else:
        json_miniklexi = get_data_from_json_file(MINIKLEXI)
        json_klexikon = get_data_from_json_file(KLEXIKON)
        json_wiki = get_data_from_json_file(WIKI)

        miniklexi = json_miniklexi["einfache"]  # label 0.0
        klexikon = json_klexikon["klexikon"]  # label 0.5
        wiki = json_wiki["wiki"]  # label 1.0

        nlp = spacy.load("de_core_news_md")
        result_miniklexi = get_features_for_lexica_corpus(miniklexi, nlp)
        result_klexikon = get_features_for_lexica_corpus(klexikon, nlp)
        result_wiki = get_features_for_lexica_corpus(wiki, nlp)

        # create a feature to index dict to keep track of order of elements
        feature_to_index = create_feature_to_idx_dict(FEATURES)

        # save results in one csv file
        header = ["#id", "#label"]
        header_features = list(feature_to_index.keys())
        header.extend(header_features)

        with open("text_complexity_lexica_corpus.csv", "w", encoding="utf-8") as csv_ofile:
            writer = csv.writer(csv_ofile, delimiter=',')
            writer.writerow(i for i in header)
            for key, value in sorted(result_miniklexi.items()):
                line = [f"miniklexi_{key}", 0.0]
                vecs = [round(i, 6) for i in value]
                line.extend(vecs)
                writer.writerow(line)
            for key, value in sorted(result_klexikon.items()):
                line = [f"klexikon_{key}", 0.5]
                vecs = [round(i, 6) for i in value]
                line.extend(vecs)
                writer.writerow(line)
            for key, value in sorted(result_wiki.items()):
                line = [f"wiki_{key}", 1.0]
                vecs = [round(i, 6) for i in value]
                line.extend(vecs)
                writer.writerow(line)

        print("Find the extracted features in text_complexity_lexica_corpus.csv")


if __name__ == "__main__":
    cli()

