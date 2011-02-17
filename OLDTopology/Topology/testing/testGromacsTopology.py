#!/usr/bin/env python

import pdb
from mmtools.Topology.GromacsTopology import *

# Tests of the Topology.GromacsTopology tools

print "Create a GromacsTopology object from file ...",
g = GromacsTopology(topfile='LG2.top')
print "Done."

print "Write 'out.top' from the contents of the GromacsTopology object ...",
g.writeTopologyFile('out.top', ExpandIncludes=False, RebuildDirectives=False)
print "Done."

print "Write 'out-expanded.top' with all of the (nested) #include files expanded ...",
g.writeTopologyFile('out-expanded.top', ExpandIncludes=True, RebuildDirectives=False)
print "Done."

print "Show all the directives defined in the GromacsTopologyFileObject:"
all_directives = g.GromacsTopologyFileObject.getAllDirectives([])
for d in all_directives:
   print '\t', d.name.strip()
print "Done."

print "Show only the ParameterDirectives:"
print 'ParameterDirectives:'
for d in g.GromacsTopologyFileObject.ParameterDirectives:
    print '\t',d.name.strip()
    #for i in range(0, len(d.lines)):
    #    print d.lines[i]

print "Show each set of MoleculeDefiniton Directive:"
for mol in range(len(g.GromacsTopologyFileObject.MoleculeDefinitionDirectives)):
  print '\tmol', mol
  for d in g.GromacsTopologyFileObject.MoleculeDefinitionDirectives[mol]:
    print '\t\t', d.name.strip()
    #for i in range(0, len(d.lines)):
    #    print d.lines[i]

print "Show the SystemDirectives:"
for d in g.GromacsTopologyFileObject.SystemDirectives:
    print '\t', d.name.strip()

#print "Show parameter contents"
#for d in g.parameters:
    #pdb.set_trace()
    #for line in d:
        #print '\t', line.directiveString()

print "Write 'out-rebuild.top' from the contents of the GromacsTopology object ...",
g.writeTopologyFile('out-rebuild.top', ExpandIncludes=False, RebuildDirectives=True)
print "Done."

pdb.set_trace()
