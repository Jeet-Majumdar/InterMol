import sys
sys.path.append('..')

from Decorators import *
from Types.AbstractBondType import *

class BondType(AbstractBondType):
    @accepts_compatible_units(None, None, None, units.nanometers, units.kilojoules_per_mole * units.nanometers**(-2), None)
    def __init__(self, atom1, atom2, type, length, k, c=0):
        AbstractBondType.__init__(self, atom1, atom2, type)
        self.length = length
        self.k = k
	self.c = c #constrained or not, Desmond
