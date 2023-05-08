MINIKLEXI = "data/miniklexi_corpus.txt"
KLEXIKON = "data/klexi_corpus.txt"
WIKI = "data/wiki_corpus.txt"
# demo
DEMO_MINIKLEXI = "demo_data/demo_miniklexi_corpus.txt"
DEMO_KLEXIKON = "demo_data/demo_klexi_corpus.txt"
DEMO_WIKI = "demo_data/demo_wiki_corpus.txt"
# tables
TOKEN_FREQ = "generated_tables/token_freq_table.json"
DISCOURSE_MARKER = "generated_tables/discourse_markers.json"
DISCOURSE_MARKER_WITH_SENSE = "generated_tables/discourse_markers_with_sense.json"
ALL_DISCOURSE_MARKER = "generated_tables/all_discourse_marker_senses.json"

FEATURES = [
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
