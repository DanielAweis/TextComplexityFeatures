# What is this work about?
This is an implementation to extract surface, syntactic, pos tag, lexical, temporal, semantic and
discourse relevant features related to text complexity. The extracted features are
stored in a CSV file. The script can be used in the command line. 

# Structure of the Repository:
* `extract_features.py`: main script which extracts the text complexity features
* `extract_features_lexica_corpus.py`: extracts the features from the lexica-corpus
* `features/`: the individual implementation of the features extraction
* `generated_tables/`: tables to calculate the lexical and the discourse features
    + token frequencies based on the DeReWo corpus: https://www.ids-mannheim.de/digspra/kl/projekte/methoden/derewo/
    + discourse marker based on the DimLex corpus:https://github.com/discourse-lab/dimlex/blob/master/DimLex-documentation.md
* `utils_and_preproces/`: scripts that generates the tables for the token frequencies and the discourse marker and utils.py
* data_analyses: 
    + `lexica_corpus_text_complexity.csv`: The result from the feature extraction for the 3 different complexity levels of the lexica-corpus.
    + `model_summaries_text_complexity.csv`: The result from the feature extraction for the summaries from the best model from (Hewett, F. and Stede, M. (2022). Extractive summarisation for german-language
data: a text-level approach with discourse features) 
    + data_analysis: TODO
* `demo_data/`: small part of the lexica-corpus to have a quick insight in the project.


# What do you need to run the code?
You need Python version 3.8. It's recommended to install the required Python packages in a virtualenv. 
You should move to the project directory if you have not already done so, create the environment with PYTHON_PATH -m venv env, and activate it with . env/bin/activate. 
Then you can continue with the installation of the required python libraries:
* To get the requirements run:  `$ pip3 install -r requirements.txt` 
* NOTE: The requirements are only for the python files not for the jupyter notebooks in in data_analysis.

After installing the requirements, you also need to download the spacy model for German:
`python -m spacy download de_core_news_sm`

# How to extract the text complexity features?
* Extract the text complexity features: `$ python extract_features.py  -p "dir_to_data/" -o "output_file_name"`
* `"dir_to_data/"` should be a path to the directory with files containing texts
* `"output_file_name"` is the file path you want to safe the results in.

# Want to have a quick insight?
* Get a demo of the features extraction with: `$ python extract_features.py -d True`

# Related Corpora:
* The Potsdam Commentary Corpus https://aclanthology.org/W04-0213/
* PCC Summaries https://github.com/fhewett/pcc-summaries
* The lexica-corpus: https://github.com/fhewett/lexica-corpus

### Author:
Daniela Weiß (This project is part of the computational linguistics BA-Thesis at the University of Potstdam. )