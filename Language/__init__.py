import json


def load(lang):
    return json.load(open(f"./Language/{lang}.json", "r"))
