class Buiding:

    def __init__(self, numberOfFloors = 0, buildingType = 'House'):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return (self.numberOfFloors == other.
numberOfFloors and self.buildingType == other.
buildingType)
