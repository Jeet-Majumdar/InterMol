

from ctools.Decorators import *
from Force.AbstractAngle import *

class Angle(AbstractAngle):

    @accepts_compatible_units(None, 
            None, 
            None, 
            units.degrees, 
            units.kilojoules_per_mole * units.radians**(-2),
            None)
    def __init__(self, atom1, atom2, atom3, theta, k, c=0):
        """
        """
        AbstractAngle.__init__(self, atom1, atom2, atom3)
        self.theta = theta
        self.k = k
        self.c = c #constrained or not, Desmond only
    
    def getForceParameters(self):
        return (self.atom1, self.atom2, self.atom3, self.theta, self.k)

    def __repr__(self):
        return str(self.atom1)+'  '+str(self.atom2)+'  '+ str(self.atom3)+'  '+ str(self.theta)+'  '+str(self.k)


    def __str__(self):
        return str(self.atom1)+'  '+str(self.atom2)+'  '+ str(self.atom3)+'  '+ str(self.theta)+'  '+str(self.k)

