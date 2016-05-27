#!/usr/bin/env python

import os
import random

def nohidden(path):
	files = os.listdir(path)
	for f in files:
		if f.startswith('.'):
			files.remove(f)
	return files

catfname = random.choice(nohidden(os.getcwd() + "/cats"))

print(catfname)
