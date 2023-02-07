from classification_to_numeric.classification_to_numeric import ClassificationToNumeric


class Residence:
    def __init__(self, dataset):
        self.dataset = dataset

    def get_all(self):
        result = set()
        for apartment in self.dataset:
            result.add(apartment['residence'])
        return result

    @staticmethod
    def map_value_to_numeric(value):
        return ClassificationToNumeric('residences/mapping.json').get_numeric(value)
