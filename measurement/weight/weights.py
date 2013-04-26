import convs
class Kilogram:
    def __init__(self, n):
        self.amount = n
    def toGram(self):
        return self.amount / convs.gramtokilogram
    def toPound(self):
        return self.toGram() / convs.poundstogram
class Gram:
    def __init__(self, n):
        self.amount = n
    def toKilogram(self):
        return self.amount * convs.gramtokilogram
    def toPound(self):
        return self.amount / convs.poundstogram
class ImpPound:
    def __init__(self, n):
        self.amount = n
    def toGram(self):
        return self.amount * convs.poundstogram
    def toKilogram(self):
        return self.amount * convs.gramtokilogram


