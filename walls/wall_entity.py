from classification_to_numeric.classification_to_numeric import ClassificationToNumeric


class Wall:
    def __init__(self, dataset):
        self.dataset = dataset

    def get_all(self):
        result = set()
        for apartment in self.dataset:
            result.add(apartment.get('attributes', {}).get('walls'))
        return result

    @staticmethod
    def map_value_to_numeric(value):
        return ClassificationToNumeric('walls/mapping.json').get_numeric(value)