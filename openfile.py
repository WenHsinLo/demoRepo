import numpy as np
import netCDF4 as nc

def openERA5(year,var):
    out = np.ones([10,10])
    return out

def timemean(var):
    return np.nanmean(var,axis=0)

