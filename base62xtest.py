#!/usr/bin/python3 
#-*- coding: utf-8 -*-

# -Base62x in -Python, testing

# Wadelau@{ufqi,gmail,hotmail}.com
# Refers to 
#    http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber=6020065
#    -GitHub-Wadelau , base62x.c
#    https://github.com/wadelau/Base62x
#    https://ufqi.com/dev/base62x/?_via=-naturedns
# since  Mon Mar  4 08:28:16 GMT 2019

import sys
import time
from datetime import date, datetime
import logging as logx

# self define modules
sys.path.append("./") # pay attention!

from Base62x import Base62x 

config = {};
base62x = Base62x(config);
base62x22 = Base62x();
