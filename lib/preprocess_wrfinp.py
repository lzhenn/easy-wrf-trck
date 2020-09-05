#/usr/bin/env python
"""Preprocessing the WRF input file"""

import configparser
import datetime
import xarray as xr
import gc

from netCDF4 import Dataset
from wrf import getvar, interplevel, ALL_TIMES 

print_prefix='lib.preprocess_wrfinp>>'

class wrf_acc_fields:

    '''
    Construct and accumulate U V W field 
    

    Attributes
    -----------
    wrf_dt: int
        input data frq from wrf raw input file(s), in seconds
    U: float
    V: float
    W: float

    Methods
    '''
    
    def __init__(self, config):
        """ construct input wrf file names """
        
        if config['INPUT'].getboolean('input_multi_files'):
            print(print_prefix+'init multi files...')
            self.strt_t=datetime.datetime.strptime(config['INPUT']['input_wrf'][-19:],'%Y-%m-%d_%H:%M:%S')

            nfiles=int(config['CORE']['integration_length'])//(int(config['INPUT']['input_file_dt'])//60)
            
            fname_prefix=config['INPUT']['input_wrf'][:-19]
            
            self.ncfiles=[]

            for ii in range(0,nfiles+1):
                fn_timestamp=self.strt_t+datetime.timedelta(hours=ii)
                self.ncfiles.append(Dataset(fname_prefix+fn_timestamp.strftime('%Y-%m-%d_%H:%M:%S')))
            self.Z = getvar(self.ncfiles, 'z',timeidx=ALL_TIMES, method="cat")
            self.U = getvar(self.ncfiles, 'ua',timeidx=ALL_TIMES, method="cat")
            self.V = getvar(self.ncfiles, 'va',timeidx=ALL_TIMES, method="cat")
            self.W = getvar(self.ncfiles, 'wa',timeidx=ALL_TIMES, method="cat")

            self.xlat = getvar(self.ncfiles[0], 'XLAT')
            self.xlon = getvar(self.ncfiles[0], 'XLONG')
            self.xh = getvar(self.ncfiles[0], 'HGT')
            self.final_t=self.strt_t+datetime.timedelta(hours=int(config['CORE']['integration_length']))

            print(print_prefix+'init multi files successfully!')

        else:
            print(print_prefix+'init from single input file...')
            self.ncfiles=Dataset(config['INPUT']['input_wrf'])
            
            print(print_prefix+'init from single input file for lat2d, lon2d, and hgt')
            self.xlat = getvar(self.ncfiles, 'XLAT')
            self.xlon = getvar(self.ncfiles, 'XLONG')
            self.xh = getvar(self.ncfiles, 'HGT')
            
            self.strt_t=datetime.datetime.utcfromtimestamp(self.xlat.Time.values.tolist()/1e9)
            self.final_t=self.strt_t+datetime.timedelta(hours=int(config['CORE']['integration_length']))
            print(print_prefix+'Init T:%s, End T:%s' %(self.strt_t.strftime('%Y-%m-%d_%H:%M:%S'), self.final_t.strftime('%Y-%m-%d_%H:%M:%S')))
            print(print_prefix+'init from single input file for Z4d')
            var_tmp = getvar(self.ncfiles, 'z',timeidx=ALL_TIMES, method="cat")
            self.Z=var_tmp

            print(print_prefix+'init from single input file for U4d')
            var_tmp = getvar(self.ncfiles, 'ua',timeidx=ALL_TIMES, method="cat")
            self.U=var_tmp
            print(print_prefix+'init from single input file for V4d')
            var_tmp = getvar(self.ncfiles, 'va',timeidx=ALL_TIMES, method="cat")
            self.V=var_tmp
            print(print_prefix+'init from single input file for W4d')
            var_tmp = getvar(self.ncfiles, 'wa',timeidx=ALL_TIMES, method="cat")
            self.W=var_tmp
            del var_tmp
            gc.collect()


            print(print_prefix+'init multi files successfully!')

if __name__ == "__main__":
    pass
