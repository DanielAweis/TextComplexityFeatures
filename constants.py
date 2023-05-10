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
            "sentence_length",
            "characters_per_word",
            "syllables_per_word",
            "text_length",
            # syntactic features
            "noun_phrases_per_sent",
            "tree_height",
            "sub_clauses_per_sent",
            "sents_with_verb_as_root",
            "sents_with_nouns_as_root",
            # POS tag features
            "POS_verbs",
            "POS_aux_verbs",
            "POS_nouns",
            "POS_adjectives",
            "POS_punctuations",
            "POS_determiners",
            "POS_pronouns",
            "POS_conjunctions",
            "POS_numerales",
            "POS_adpositions",
            # lexical features
            "ttr",
            "lexical_complexity_score",
            # verb tense
            "verbs_in_sentence",
            # semantic_similarity_features
            "semantic_similarity_nouns",
            "semantic_similarity_verbs",
            "semantic_similarity_adjectives",
            # discourse features
            "pronouns_per_sentence",
            "articles_per_sentence",
            "count_of_discourse_markers",
            # discourse marker senses
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
