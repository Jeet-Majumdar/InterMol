import sys
sys.path.append('..')

from Decorators import *
from Types.AbstractDihedralType import *

class RBDihedralType(AbstractDihedralType):

    @accepts_compatible_units(None,
            None,
            None,
            None,
            None,
            units.kilojoules_per_mole,
            units.kilojoules_per_mole,
            units.kilojoules_per_mole,
            units.kilojoules_per_mole,
            units.kilojoules_per_mole,
            units.kilojoules_per_mole)
    def __init__(self, atom1, atom2, atom3, atom4, type, C0, C1, C2, C3, C4, C5):
        """
        """
        AbstractDihedralType.__init__(self, atom1, atom2, atom3, atom4, type)
        self.C0 = C0
        self.C1 = C1
        self.C2 = C2
        self.C3 = C3
        self.C4 = C4
        self.C5 = C5
