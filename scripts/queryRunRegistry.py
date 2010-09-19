#!/usr/bin/env python

import gcSupport
from grid_control.CMSSW import formatLumi, parseLumiFromJSON, cmpLumi
import xmlrpclib

server = xmlrpclib.ServerProxy('http://pccmsdqm04.cern.ch/runregistry/xmlrpc')
data = server.DataExporter.export('RUNLUMISECTION', 'GLOBAL', 'json', {'groupName': 'Collisions10'})
runs = parseLumiFromJSON(data)
runs.sort(cmpLumi)

print("lumi filter =")
for line in map(lambda x: str.join(", ", x), gcSupport.utils.lenSplit(formatLumi(runs), 60)):
	print("\t%s" % line)