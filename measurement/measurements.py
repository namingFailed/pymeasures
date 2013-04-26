#also need cup and spoon conversion 
#functions as well as these
#
#the measurements will need to
#be enum for db entry
class Measurement:
    class LengthMeasure:
        class Metre: pass
        class Inch: pass
        class Foot: pass
    class WeightMeasure:
        class Kilogram: pass
        class Gram: pass
        class ImpPound: pass
    class VolumeMeasure:
        class Litre: pass
        class Millelitre: pass
        class Cup: pass
        class Teaspoon: pass
        class TableSpoon: pass
    class ItemMeasure:
        class thickSlice: pass
        class medSlice: pass
        class thinSlice: pass


