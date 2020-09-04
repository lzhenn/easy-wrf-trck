#/usr/bin/env python
'''
Date: Sep 2, 2020


Zhenning LI

'''

from netCDF4 import Dataset
from wrf import getvar
import numpy as np
import csv
import configparser
import sys
sys.path.append('../')
import lib.read_ini


def get_closest_idx_xy(lat2d, lon2d, lat_array, lon_array):
    """
        Find the nearest x,y in lat2d and lon2d for lat_arry and lon_array
    """
    idx=[]
    for (lat0, lon0) in zip(lat_array, lon_array):
        dis_lat2d=lat2d-lat0
        dis_lon2d=lon2d-lon0
        dis=abs(dis_lat2d)+abs(dis_lon2d)
        idx.append(np.argwhere(dis==dis.min())[0].tolist()) # x, y position
    return idx #[[x0,y0],[x1,y1]] 


if __name__ == "__main__":
    
    init_height=100
    
    print('Read Config...')
    config=lib.read_ini.read_cfg('./conf/config.ini')
     if config['INPUT'].getboolean('input_multi_files'):
        strt_time=datetime.datetime.strptime(config['INPUT']['input_wrf'][-19:],'%Y-%m-%d_%H:%M:%S')
        nfiles=int(config['CORE']['integration_length'])//(int(config['INPUT']['input_file_dt'])//60)
        
        fname_prefix=config['INPUT']['input_wrf'][:-19]
        
        self.ncfiles=[]

        for ii in range(0,nfiles+1):
            fn_timestamp=strt_time+datetime.timedelta(hours=ii)
            self.ncfiles.append(Dataset(fname_prefix+fn_timestamp.strftime('%Y-%m-%d_%H:%M:%S')))

 
    self.t0=datetime.datetime.strptime(config['INPUT']['input_wrf'][-19:],'%Y-%m-%d_%H:%M:%S')
    self.dt=datetime.timedelta(minutes=int(config['CORE']['time_step']))

   
    restime = getvar(ncfile, 'LANDMASK') # as template
    xlat = getvar(ncfile, 'XLAT')
    xlon = getvar(ncfile, 'XLONG')

    restime.name='ResTime'
    restime.values.fill(0) # reset to zero

    restime_frm=restime.values

    
    print(restime)      
