from __future__ import print_function, division
import datetime
from PyAstronomy import pyasl
import numpy as np

# Convert calendar date to JD
# using the datetime package
jd = datetime.datetime(1995, 11, 4)
jd = pyasl.jdcnv(jd)
jd = np.arange(jd, jd + 20, 1)
# Calculate Moon positions
res = pyasl.moonpos(jd)

print("%15s  %8s  %8s  %11s  %8s  %8s" %
      ("JD", "RA", "DEC", "DIST", "GEOLON", "GEOLAT"))
print("%15s  %8s  %8s  %11s  %8s  %8s" %
      ("[d]", "[deg]", "[deg]", "[km]", "[deg]", "[deg]"))
for i in range(jd.size):
    print("%15.4f  %8.4f  %8.4f  %11.4f  %8.4f  %8.4f" %
          (jd[i], res[0][i], res[1][i], res[2][i], res[3][i], res[4][i]))