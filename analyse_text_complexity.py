from os import scandir
from pathlib import Path
import spacy
from extract_features import calculate_all_features
from utils import save_to_json_file


def extract_features_for_all_docs(directory_path, nlp):
    """
    Extracts for all documents in the directory the text complexity features
    and saves this in a feature vector (list of nums).

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
                doc = nlp(text)
                feature_vector = calculate_all_features(doc, nlp)
                results[document.name.strip(".txt")] = feature_vector

    return results


def main():
    summaries_dir_path = "data/model_summaries/"
    nlp = spacy.load("de_core_news_md")
    text_complexity_features = extract_features_for_all_docs(summaries_dir_path, nlp)
    save_to_json_file(text_complexity_features, "text_complexity_feature_vectors.json")


if __name__ == '__main__':
    main()