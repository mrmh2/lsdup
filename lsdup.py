#!/usr/bin/env python

import os
import hashlib
import subprocess

class Ftree:
	def __init__(self):
		pass

dirtree = {}
hashtable = {}
fcount = 0

for dirpath, dirnames, filenames in os.walk('/Users/hartleym/Code'):
#for dirpath, dirnames, filenames in os.walk('/Users/hartleym/test/lsdup'):
	#print dirpath, dirnames, filenames
	dirtree[dirpath] = {}
	dirtree[dirpath]['dchildren'] = dirnames
	dirtree[dirpath]['fchildren'] = filenames
	fcount = fcount + len(filenames)
	#dirtreeI

print "Read %d directories, %d files" % (len(dirtree), fcount)

for d in dirtree:
	#for dc in dirtree[d]['dchildren']:
	#	print os.path.join(d, dc)
	dirtree[d]['dchildren'] = [os.path.join(d, dc) for dc in dirtree[d]['dchildren']]
	#for f in dirtree[d]['fchildren']:
	#	print [os.path.join(d, f) for f in dirtree[d]['fchildren']]

hcount = 0

for d in dirtree:
	for f in  dirtree[d]['fchildren']:
		md5sum = subprocess.check_output(["md5", "-q", os.path.join(d, f)])
		if md5sum in hashtable:
			#print os.path.join(d,f), "is", hashtable[md5sum]
			pass
			
		else:
			hashtable[md5sum] = os.path.join(d,f)
			hcount = hcount + 1
		#print md5sum.strip()
		print hcount, "/", fcount

#print dirtree
