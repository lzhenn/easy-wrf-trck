#/usr/bin/env python
'''
Date: Sep 2, 2020

Take landsea mask from wrf output and construct input.csv by all ocean grid

Zhenning LI

'''

from netCDF4 import Dataset
from wrf import getvar
import numpy as np
import csv

if __name__ == "__main__":
    
    init_height=100
    ncfile=Dataset("/home/dataop/data/nmodel/wrf_2doms_enlarged/2016/201601/2016010112/wrfout_d01_2016-01-02_12:00:00")
    
    lsmask = getvar(ncfile, 'LANDMASK')
    xlat = getvar(ncfile, 'XLAT')
    xlon = getvar(ncfile, 'XLONG')

    xlat=xlat.where(lsmask==0)
    xlon=xlon.where(lsmask==0)

    xlat1d=xlat.values[~np.isnan(xlat.values)].flatten()
    xlon1d=xlon.values[~np.isnan(xlon.values)].flatten()
    igrid=0
    with open('../input/input.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for ilat, ilon in zip(xlat1d, xlon1d):
            spamwriter.writerow([igrid, ilat, ilon, init_height])
            igrid=igrid+1
        
