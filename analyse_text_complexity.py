import spacy
import csv
import click

from os import scandir
from pathlib import Path

from extract_features import calculate_features, create_feature_to_idx_dict

from utils_and_preprocess.constants import FEATURES
from utils_and_preprocess.utils import validate_doc


def extract_features_for_all_docs(directory_path, nlp):
    """
    Extracts the text complexity features for all documents in the directory
    and saves this in a dict with file name as keys and feature vector (list of nums)
    as value.

    :param directory_path: str
    :param nlp: spacy model
    :return: dict
    """
    results = dict()
    with scandir(directory_path) as documents:
        for document in documents:
            if document.name.endswith(".txt"):
                temp_inputfile = Path(directory_path + document.name)
                text = temp_inputfile.read_text(encoding="utf-8")

                is_valid = validate_doc(text, nlp)
                if not is_valid:
                    print(f"The file {document.name} is invalid.")
                    continue

                doc = nlp(text)
                feature_vector = calculate_features(doc, nlp)
                results[document.name.strip(".txt")] = feature_vector

    return results


@click.command()
@click.option("-d", "demo", type=bool, default=False, help="If you want to see a small demo.")
@click.option("-p", "directory_path", type=str, default=True, help="The directory path (str)"
                                                                   " - containing the documents with"
                                                                   " texts for which the text complexity"
                                                                   " features are to be extracted.")
@click.option("-o", "output_path", type=str, default=True, help="The path (str) for the output file "
                                                                "in which the extracted features are "
                                                                "saved as a dataframe in csv format.")
def cli(demo, directory_path, output_path):
    if demo:
        play_demo()
    else:
        #summaries_dir_path = "data/model_summaries/"
        nlp = spacy.load("de_core_news_md")
        text_complexity_features = extract_features_for_all_docs(directory_path, nlp)

        # create a feature to index dict to keep track of order of elements
        feature_to_index = create_feature_to_idx_dict(FEATURES)

        # save results in one csv file
        header = ["#id"]
        header_features = list(feature_to_index.keys())
        header.extend(header_features)

        with open(output_path, "w", encoding="utf-8") as csv_ofile:
            writer = csv.writer(csv_ofile, delimiter=',')
            writer.writerow(i for i in header)
            for key, value in sorted(text_complexity_features.items()):
                line = [key]
                vecs = [round(i, 6) for i in value]
                line.extend(vecs)
                writer.writerow(line)


@click.command()
@click.option("-demo", "demo", type=bool, default=False, help="If you want to see a small demo.")
@click.option("-d", "directory_path", type=str, default=True, help="The directory path (str) - containing the documents with texts for which the text complexity features are to be extracted.")
@click.option("-o", "output_path", type=str, default=True, help="The path (str) for the output file in which the extracted features are saved as a dataframe in csv format.")
def test_main(directory_path, output_path):
    print(directory_path)
    print(output_path)


def play_demo():
    print("demo")


if __name__ == '__main__':
    cli()
