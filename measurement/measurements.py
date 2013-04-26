#also need cup and spoon conversion 
#functions as well as these
#
#the measurements will need to
#be enum for db entry
class Measurement:
    pass
class LengthMeasure(Measurement):
    pass
class Metre(LengthMeasure): 
    pass
class Inch(LengthMeasure): 
    pass
class Foot(LengthMeasure): 
    pass
class WeightMeasure(Measurement):
    pass
class Kilogram(WeightMeasure):
    pass
class Gram(WeightMeasure): 
    pass
class ImpPound(WeightMeasure): 
    pass
class VolumeMeasure(Measurement):
    pass
class Litre(VolumeMeasure): 
    pass
class Millelitre(VolumeMeasure): 
    pass
class Cup(VolumeMeasure): 
    pass
class Teaspoon(VolumeMeasure): 
    pass
class TableSpoon(VolumeMeasure): 
    pass
class ItemMeasure(Measurement):
    pass
class thickSlice(ItemMeasure): 
    pass
class medSlice(ItemMeasure): 
    pass
class thinSlice(ItemMeasure): 
    pass
