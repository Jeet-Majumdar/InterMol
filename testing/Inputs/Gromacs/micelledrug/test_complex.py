import ctools.Driver as Driver
import pdb
Driver.initSystem("Solvated Micelle")

Driver.loadTopology("complex.top")
Driver.loadStructure("complex.gro")

Driver.writeStructure("complex_out.gro")
Driver.writeTopology("complex_out.top")


