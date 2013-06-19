#!/usr/bin/env python
"""Look for duplicate directory trees within a directory tree.
"""

import os
import sys
from pprint import pprint

def build_dir_dict(path):
    """Generate a dictionary keyed by the dirnames in the tree. Values are a
    dictionary which will be used to distinguish directories. Initial entry in
    this dictionary is a count of the objects (files + directories) in the
    directory."""

    return { dirpath: {'objcount': len(dirnames + filenames),
                       'filenames' : filenames,
                       'dirnames' : dirnames}
            for dirpath, dirnames, filenames
            in os.walk(path)
            if len(dirnames + filenames)
            }

def rekey(dd):

    entryd = {}
    dupd = {}

    dupcount = 0

    for entry, vals in dd.items():
        new_key = ''.join(vals['filenames'] + vals['dirnames'])
        if new_key not in entryd:
            entryd[new_key] = entry
        else:
            dupd[entry] = 1

    print len(dupd)

    return entryd

def main():
    try:
        path = sys.argv[1]
    except IndexError:
        path = 'test'
        
    dd = build_dir_dict(path)

    #pprint(dd)

    dupd = rekey(dd)

    print len(dd), len(dupd)

if __name__ == '__main__':
    main()
