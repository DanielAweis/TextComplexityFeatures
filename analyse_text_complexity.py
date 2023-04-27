from os import scandir
from pathlib import Path
import spacy
from extract_features import calculate_all_features
from utils_and_preprocess.utils import save_to_json_file, check_input_validity


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
                try:
                    check_input_validity(document.name, text, nlp)
                    doc = nlp(text)
                    feature_vector = calculate_all_features(doc, nlp)
                    results[document.name.strip(".txt")] = feature_vector
                except:
                    continue

    return results


def main():
    summaries_dir_path = "data/small_sum/"
    nlp = spacy.load("de_core_news_md")
    text_complexity_features = extract_features_for_all_docs(summaries_dir_path, nlp)
    save_to_json_file(text_complexity_features, "text_complexity_feature_vectors.json")


if __name__ == '__main__':
    main()