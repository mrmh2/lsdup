#!/usr/bin/env python

import os, pprint



def build_direntry(dirpath, dirnames, filenames):
	d = {}
	d['dchildren'] = [os.path.join(dirpath, dn) for dn in dirnames]
	d['fchildren'] = [{os.path.join(dirpath, fn): 0} for fn in filenames]
	#print fcs
	#for fc in fcs:
	#	print {fc: 0}

	return d

def build_dirtree(rootpath):

	dtree = {}
	for dirpath, dirnames, filenames in os.walk(rootpath):
		#files += [os.path.join(dirpath, f) for f in filenames]
		dtree[dirpath] = build_direntry(dirpath, dirnames, filenames)

	for d in dtree:
		for dc in dtree[d]['dchildren']:
			dtree[dc]['parent'] = d

	return dtree

def tag_file_in_tree(dtree, filename):
	for d in dtree:
		for fc in dtree[d]['fchildren']:
			#print "TESTING %s AGAINST %s" % (fc, filename)
			if filename in fc:
				#print "MATCH"
				fc[filename] = 1

rootpath = "/Users/hartleym/test/lsdup"
dtree = build_dirtree(rootpath)

filename = '/Users/hartleym/test/lsdup/dir1/file3'


	
pprint.pprint(dtree)
tag_file_in_tree(dtree, filename)
pprint.pprint(dtree)
