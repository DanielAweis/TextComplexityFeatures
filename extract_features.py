# This script extracts surface, syntactic, pos tag, lexical, temporal, semantic and
# discourse relevant features related to text complexity. The extracted features are
# stored in a CSV file. The script can be used in the command line. The parameters
# to be specified are the path to the folder containing the texts from which the
# features are to be extracted. And the name of the file in which the results are to
# be saved. An example call of the script could look like this:
# $ python extract_features.py  -p "dir_to_data/" -o "output_file_name"
import spacy
import click
import csv

from os import scandir
from pathlib import Path

# The list of all features can be found in the file utils.constants
# under FEATURES. This also facilitates the quick adjustment of the
# feature set.
from constants import FEATURES
from utils_and_preprocess.utils import validate_doc, get_data_from_json_file

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

from constants import TOKEN_FREQ
# based on the DeReWo corpus
# https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/

from features.lexical_features import calculate_ttr, \
    calculate_lexical_complexity_score

from features.verb_tense_feature import get_average_number_of_verbs_in_sentence

from features.semantic_similarity_features import \
    get_average_semantic_similarity_of_all_nouns, \
    get_average_semantic_similarity_of_all_verbs, \
    get_average_semantic_similarity_of_all_adjectives

from constants import DISCOURSE_MARKER, \
    DISCOURSE_MARKER_WITH_SENSE, ALL_DISCOURSE_MARKER

from features.discourse_features import \
    get_average_count_of_pronouns_per_sentence, \
    get_average_count_of_definite_articles_per_sentence, \
    get_average_count_of_discourse_markers_per_sentence, \
    get_count_for_discourse_marker_senses


def create_feature_to_idx_dict(features):
    """Creates a dictionary that maps each feature to its index in the input list
     to keep track of order of elements and for the header for the data frame.

    :param features: A list of features.
    :return: dict
    """
    feature_to_index = dict()
    for i, value in enumerate(features):
        feature = "".join(value)
        feature_to_index[feature] = i

    return feature_to_index


def calculate_features(doc, nlp, tokens_freq, discourse_marker):
    """Calls all functions that extract the linguistic features of text complexity.
    Returns a list of numbers (vector). If the list of features to be extracted
    changes, then the order here and in utils.constants FEATURES must be aligned.

    :param doc: spacy.tokens.doc.Doc
    :param nlp: spacy model
    :param tokens_freq: token frequencies dict
    :param discourse_marker: dict of discourse markers and senses
    :return: a list of numbers
    """
    result = [
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
            calculate_lexical_complexity_score(doc, tokens_freq),
            # verb tense
            get_average_number_of_verbs_in_sentence(doc),
            # semantic_similarity_features
            get_average_semantic_similarity_of_all_nouns(doc, nlp),
            get_average_semantic_similarity_of_all_verbs(doc, nlp),
            get_average_semantic_similarity_of_all_adjectives(doc, nlp),
            # discourse features
            get_average_count_of_pronouns_per_sentence(doc),
            get_average_count_of_definite_articles_per_sentence(doc),
            get_average_count_of_discourse_markers_per_sentence(doc, discourse_marker["disc_marker"])
            ]
    # this returns a vector
    dms_vec = get_count_for_discourse_marker_senses(doc, discourse_marker["all_disc_marker_senses"],
                                                    discourse_marker["discourse_markers_with_sense"])
    # extend the result vector with the discourse marker senses vector
    result.extend(dms_vec)
    return result


def extract_features_for_all_docs(directory_path, nlp, tokens_freq, discourse_marker):
    """Extracts the text complexity features for all documents in the directory
    and saves this in a dict with file name as keys and feature vector (list of nums)
    as value.

    :param directory_path: str
    :param nlp: spacy model
    :param tokens_freq: token frequencies dict
    :param discourse_marker: dict of discourse markers and senses
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
                feature_vector = calculate_features(doc, nlp, tokens_freq, discourse_marker)
                results[document.name.strip(".txt")] = feature_vector

    return results


def play_demo():
    nlp = spacy.load("de_core_news_md")
    text = "Das ist meine tolle Banane. " \
           "Die Banane ist reif. " \
           "Sie existiert, um gegessen zu werden. " \
           "Je toller eine Banane ist, desto mehr möchte ich sie essen. " \
           "Sie kann gegessen werden, weil sie essbar ist. " \
           "Gurken und Bananen machen mich glücklich, obwohl sie aus Fasern bestehen. "
    doc = nlp(text)

    tokens_freq = get_data_from_json_file(TOKEN_FREQ)

    disc_marker = get_data_from_json_file(DISCOURSE_MARKER)
    discourse_markers_with_sense = get_data_from_json_file(DISCOURSE_MARKER_WITH_SENSE)
    all_disc_marker_senses = get_data_from_json_file(ALL_DISCOURSE_MARKER)
    discourse_marker = {
        "disc_marker": disc_marker,
        "discourse_markers_with_sense": discourse_markers_with_sense,
        "all_disc_marker_senses": all_disc_marker_senses
    }

    vec = calculate_features(doc, nlp, tokens_freq, discourse_marker)
    feature_to_index = create_feature_to_idx_dict(FEATURES)
    header_features = list(feature_to_index.keys())
    print("#### DEMO TEXT COMPLEXITY FEATURE EXTRACTION #####")
    print(text)
    print("EXTRACTED FEATURES:")
    print(header_features)
    print(vec)
    print("#### END ####")


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
        print("#### TEXT COMPLEXITY FEATURE EXTRACTION #####")
        #summaries_dir_path = "data/model_summaries/"
        tokens_freq = get_data_from_json_file(TOKEN_FREQ)
        disc_marker = get_data_from_json_file(DISCOURSE_MARKER)
        discourse_markers_with_sense = get_data_from_json_file(DISCOURSE_MARKER_WITH_SENSE)
        all_disc_marker_senses = get_data_from_json_file(ALL_DISCOURSE_MARKER)
        discourse_marker = {
            "disc_marker": disc_marker,
            "discourse_markers_with_sense": discourse_markers_with_sense,
            "all_disc_marker_senses": all_disc_marker_senses
        }

        nlp = spacy.load("de_core_news_md")
        text_complexity_features = extract_features_for_all_docs(directory_path, nlp, tokens_freq, discourse_marker)

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

    print("Find the extracted features in ", output_path)
    print("#### END ####")


if __name__ == "__main__":
    cli()
