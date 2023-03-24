import json


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