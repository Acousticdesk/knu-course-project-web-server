import json
import os


class ClassificationToNumeric:
    def __init__(self, path_to_mapping):
        mapping = open(os.path.join(os.getcwd(), path_to_mapping))
        self.data = json.load(mapping)

    def get_numeric(self, value):
        return self.data.index(value)