import json


def file_path_name_w_ext(file_name, path=None):
    if path is None:
        file_path = './'
    else:
        file_path = './' + path + '/'

    if file_name.endswith(".json"):
        path_name_w_ext = file_path + file_name
    else:
        path_name_w_ext = file_path + file_name + '.json'

    return path_name_w_ext


def writeJSONfile(file_name, data, path=None):
    with open(file_path_name_w_ext(file_name, path), 'w') as fp:
        json.dump(data, fp)


def getJSONfile(file_name, path=None):
    with open(file_path_name_w_ext(file_name, path), 'r') as fp:
        return json.load(fp)
