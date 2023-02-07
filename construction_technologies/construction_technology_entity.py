from classification_to_numeric.classification_to_numeric import ClassificationToNumeric


class ConstructionTechnology:
    def __init__(self, dataset):
        self.dataset = dataset

    def get_all(self):
        result = set()
        for apartment in self.dataset:
            result.add(apartment.get('attributes', {}).get('construction_technology'))
        return result

    @staticmethod
    def map_value_to_numeric(value):
        return ClassificationToNumeric('construction_technologies/mapping.json').get_numeric(value)
