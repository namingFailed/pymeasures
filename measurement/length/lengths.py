import convs
import math
class Metre:
    def __init__(self, n):
        self.amount = n
    def toFeet(self):
        return self.amount / convs.foottometre
    def toInch(self):
        return (self.amount / convs.foottometre) / convs.inchtofoot
    def toFeetandInches(self):
        inches = self.toInch()
        ffeet = math.floor(inches / (1/convs.inchtofoot))
        feet, partfeet= divmod(inches, 1/convs.inchtofoot)
        return feet, partfeet
class Foot:
    def __init__(self, n):
        self.amount = n
    def toInch(self):
        return self.amount / convs.inchtofoot
    def toMetre(self):
        return self.amount * convs.foottometre
class Inch:
    def __init__(self, n):
        self.amount = n
    def toFeet(self):
        return self.amount * convs.inchtofoot
    def toMetre(self):
        return self.toFeet() * convs.foottometre
