import json
import csv


def get_data_from_json_file(json_file_path):
    """Returns data as json object.
    :param json_file_path: (str)
    :return: dict """
    with open(json_file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def save_to_json_file(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)


def add_nummeric_label(vectores_file_path):
    # "data/feature_vectors_L.csv"
    data = []
    with open(vectores_file_path, "r", encoding="utf-8") as file:
        for line in file:
            new_line = []
            if line.startswith("#"):
                new_array = ["#label"]
                new_array.extend(line.split(","))
                line = new_array
                data.append(new_array)
            elif line.split(",")[0].startswith("miniklexi_"):
                new_array = ["0.0"]
                new_array.extend(line.split(","))
                data.append(new_array)
            elif line.split(",")[0].startswith("klexikon_"):
                new_array = ["0.5"]
                new_array.extend(line.split(","))
                data.append(new_array)
            elif line.split(",")[0].startswith("wiki_"):
                new_array = ["1.0"]
                new_array.extend(line.split(","))
                data.append(new_array)

    header = data[0]
    with open("data/feature_df.csv", "w", encoding="utf-8") as csv_ofile:
        writer = csv.writer(csv_ofile, delimiter=',')
        writer.writerow(i for i in header)
        for line in data[1:]:
            writer.writerow(line)
