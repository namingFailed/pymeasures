import inspect
import sys
from utilities import makeMeasureEnum
from weight import weights
from length import lengths
from volume import volumes
from item import items
tmp=makeMeasureEnum(globals().items())
global MeasurementEnum
global ReverseMeasurementEnum 
MeasurementEnum = tmp[0]
ReverseMeasurementEnum = tmp[1]
print ReverseMeasurementEnum
