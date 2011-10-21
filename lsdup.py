#!/usr/bin/env python

import os
import hashlib
import subprocess
import pprint

def md5sum_from_filename(filename):
		return subprocess.check_output(["md5", "-q", filename]).strip()

def find_duplicates(files, comparator):
# TODO - make this less ugly
	sizes = {}
	dups = {}

	for f in files:
		sz = comparator(f)
		if sz in sizes:
			if sz in dups:
				dups[sz]['rc'] += 1
				dups[sz]['r'] += [f]
			else:
				# Initialise new entry in duplicates with a reference count of 2 and the known references
				dups[sz] = {'rc': 2, 'r': [sizes[sz], f]}
		else:
			sizes[sz] = f

	return dups

def list_from_dups(dups):
	l = []
	for d in dups:
		l += [r for r in dups[d]['r']]
	return l

rootpath = '/Users/hartleym/Code'
print "Building file list..."

files = []
for dirpath, dirnames, filenames in os.walk(rootpath):
	files += [os.path.join(dirpath, f) for f in filenames]
print "...%d found" % len(files)

print "Building candidate duplicates list..."
kdups_bysize = find_duplicates(files, os.path.getsize)
ldups_bysize = list_from_dups(kdups_bysize)
print "...%d found" % len(ldups_bysize)
#print ldups_bysize
print "Calculating hash collisions..."
kdups_byhash = find_duplicates(ldups_bysize, md5sum_from_filename)
ldups_byhash = list_from_dups(kdups_byhash)
print "...%d found" % len(ldups_byhash)

for h in kdups_byhash:
	for d in kdups_byhash[h]['r']:
		print "=%s" % d
	print ""


#md5sums = {}
#mdups = {}
#print "Calculating hashes"
#for d in dups:
#	for f in dups[d]['r']:
#		md = md5sum_from_filename(f)
#		if md in md5sums:
#			if md in mdups:
#				mdups[md]['rc'] += 1
#				mdups[md]['r'] += [f]
#			else:
#				mdups[md] = {'rc': 2, 'r': [sizes[sz], f]}
#		else:
#			md5sums[md] = f
#
##print "%d collisions found" % len(mdups)
#
#for d in mdups:
#	rc = mdups[d]['rc']
#	if rc > 5:
#		pass
#		#print mdups[d]
#
#dirtree = {}
#hashtable = {}
#fcount = 0
#
#for dirpath, dirnames, filenames in os.walk('/Users/hartleym/Code'):
##for dirpath, dirnames, filenames in os.walk('/Users/hartleym/test/lsdup'):
#	#print dirpath, dirnames, filenames
#	dirtree[dirpath] = {}
#	dirtree[dirpath]['dchildren'] = dirnames
#	dirtree[dirpath]['fchildren'] = filenames
#	fcount = fcount + len(filenames)
#	#dirtreeI
#
#print "Read %d directories, %d files" % (len(dirtree), fcount)
#
#for d in dirtree:
#	#for dc in dirtree[d]['dchildren']:
#	#	print os.path.join(d, dc)
#	dirtree[d]['dchildren'] = [os.path.join(d, dc) for dc in dirtree[d]['dchildren']]
#	#for f in dirtree[d]['fchildren']:
#	#	print [os.path.join(d, f) for f in dirtree[d]['fchildren']]
#
#hcount = 0
#
#for d in dirtree:
#	for f in  dirtree[d]['fchildren']:
#		md5sum = subprocess.check_output(["md5", "-q", os.path.join(d, f)])
#		if md5sum in hashtable:
#			#print os.path.join(d,f), "is", hashtable[md5sum]
#			pass
#			
#		else:
#			hashtable[md5sum] = os.path.join(d,f)
#			hcount = hcount + 1
#		#print md5sum.strip()
#		print hcount, "/", fcount
#
##print dirtree
