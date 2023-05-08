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
            # semantic_similarity_features
            "average_semantic_similarity_of_all_nouns",
            "average_semantic_similarity_of_all_verbs",
            "average_semantic_similarity_of_all_adjectives",
            # discourse features
            "average_count_of_pronouns_per_sentence",
            "average_count_of_definite_articles_per_sentence",
            "average_count_of_discourse_markers_per_sentence",
            # discourse marker senses
            "",
            "Contingency.Cause.Reason",
            "Expansion.Substitution.Arg2-as-subst",
            "Contingency.Cause.Result",
            "Contingency.Purpose.Arg1-as-goal",
            "Expansion.Conjunction",
            "Temporal.Asynchronous.Succession",
            "Comparison.Contrast",
            "Temporal.Asynchronous.Precedence",
            "Expansion.Exception.Arg2-as-except",
            "Comparison.Concession.Arg1-as-denier",
            "Contingency.Negative-condition.Arg2-as-negCond",
            "Expansion.Disjunction",
            "Expansion.Manner.Arg1-as-manner",
            "Expansion.Level-of-detail.Arg1-as-detail",
            "Contingency.Negative-condition.Arg1-as-negCond",
            "Comparison.Concession.Arg2-as-denier",
            "Temporal.Synchronous",
            "Contingency.Purpose.Arg2-as-goal",
            "Expansion.Exception.Arg1-as-except",
            "Expansion.Instantiation",
            "Expansion.Level-of-detail.Arg2-as-detail",
            "Expansion.Substitution.Arg1-as-subst",
            "Contingency.Condition.Arg1-as-cond",
            "Expansion.Instantiation.Arg2-as-instance",
            "Contingency.Condition.Arg2-as-cond",
            "Expansion.Equivalence",
            "Expansion.Manner.Arg2-as-manner"
            ]
