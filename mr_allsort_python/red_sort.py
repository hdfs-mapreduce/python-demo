#!/usr/local/bin/python

import sys

for line in sys.stdin:
    idx_id, key, val = line.strip().split('\t')
    print '\t'.join([key, val])

