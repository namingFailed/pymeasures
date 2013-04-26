class Litre:
    def __init__(self, n):
        self.amount = n
    def toMl(self):
        return self.amount / convs.millelitretolitre
    def toCup(self):
        return (self.toMl() / convs.cuptomillelitre)
    def toPint(self):
        return self.amount * convs.litretopint
    def toGallon(self):
        return self.amount * convs.litretogallon
class Millelitre:
    def __init__(self, n):
        self.amount = n
    def toLitre(self):
        return self.amount * convs.millelitretolitre
    def toCl(self):
        return self.amount * convs.millelitretocentilitre
    def toCup(self):
        return self.amount / convs.cuptomillelitre
    def toTablespoon(self):
        return self.amount / convs.tablespoontomillelitre
    def toTeaspoon(self):
        return self.amount / convs.teaspoontomillelitre
    def toShot(self):
        return self.amount / convs.shottomillelitre
class Teaspoon:
    def __init__(self, n):
        self.amount = n
    def toTablespoon(self):
        return self.amount * convs.teaspoontotablespoon
    def toMl(self):
        return self.amount * convs.teaspoontomillelitre
    def toShot(self):
        return self.toMl() / convs.shottomillelitre
class Tablespoon:
    def __init__(self, n):
        self.amount = n
    def toMl(self):
        return self.amount * convs.tablespoontomillelitre
    def toTeaspoon(self):
        return self.amount / convs.teaspoontotablespoon
    def toCup(self):
        return self.amount * convs.tablespoontocup
    def toShot(self):
        return self.toMl() / convs.shottomillelitre
class Cup:
    def __init__(self, n):
        self.amount = n
    def toMl(self):
        return self.amount * convs.cuptomillelitre
    def toLitre(self):
        return self.toMl() * convs.millelitretolitre 
    def toTablespoon(self):
        return self.amount / convs.tablespoontocup
    def toShot(self):
        return self.toMl() / convs.shottomillelitre
class Shot:
    def __init__(self, n):
        self.amount = n
    def toMl(self):
        return self.amount * convs.shottomillelitre  
    def toTablespoon(self):
        return self.toMl() / convs.tablespoontomillelitre
    def toTeaspoon(self):
        return self.toMl() / convs.teaspoontomillelitre
    def toCup(self):
        return self.toMl() / convs.cuptomillelitre
    def toCl(self):
        return self.toMl() * convs.millelitretolitre
