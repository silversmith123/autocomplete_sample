# coding: utf-8
import sys, os
import bottle

dirpath = os.path.dirname(os.path.abspath(__file__))
print(dirpath)
sys.path.append(dirpath)
os.chdir(dirpath)

import suggest
application = bottle.default_app()