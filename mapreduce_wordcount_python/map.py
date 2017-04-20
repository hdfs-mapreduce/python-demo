#!/usr/local/bin/python

import sys

for line in sys.stdin:
	ss = line.strip().split(' ')
	for s in ss:
		if s.strip() != "":
			print "%s\t%s" % (s, 1)
