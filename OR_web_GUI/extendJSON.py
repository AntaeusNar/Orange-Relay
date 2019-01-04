import json


def writeJSONfile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def getJSONfile(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)