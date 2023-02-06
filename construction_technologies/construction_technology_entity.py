class ConstructionTechnology:
    def __init__(self, dataset):
        self.dataset = dataset

    def get_all(self):
        result = set()
        for apartment in self.dataset:
            result.add(apartment['attributes']['construction_technology'])
        return result
