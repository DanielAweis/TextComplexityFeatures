# What is this work about?
This is an implementation to extract surface, syntactic, pos tag, lexical, temporal, semantic and
discourse relevant features related to text complexity. The extracted features are
stored in a CSV file. The script can be used in the command line. 

# What do you need to run the code?
* To get the requirements run:  `$ pip3 install -r requirements.txt` 

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