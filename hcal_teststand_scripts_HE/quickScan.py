import sys
import subprocess

from hcal_teststand.uhtr import *
from hcal_teststand import *
from hcal_teststand.hcal_teststand import *
from hcal_teststand.qie import *

from read_histo import *

ts = teststand("HEfnalAcc")


uhtr.get_histos(ts=ts, n_orbits=1000, sepCapID=1, file_out_base="histotest")

vals = read_histo("histotest.root",True,0)



for i in vals:
    print i, vals[i]

