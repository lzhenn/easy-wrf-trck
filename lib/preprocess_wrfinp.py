#/usr/bin/env python
"""Preprocessing the WRF input file"""

import configparser
import datetime
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
            strt_time=datetime.datetime.strptime(config['INPUT']['input_wrf'][-19:],'%Y-%m-%d_%H:%M:%S')

            nfiles=int(config['CORE']['integration_length'])//(int(config['INPUT']['input_file_dt'])//60)
            
            fname_prefix=config['INPUT']['input_wrf'][:-19]
            
            self.ncfiles=[]

            for ii in range(0,nfiles+1):
                fn_timestamp=strt_time+datetime.timedelta(hours=ii)
                self.ncfiles.append(Dataset(fname_prefix+fn_timestamp.strftime('%Y-%m-%d_%H:%M:%S')))
        else:
                self.ncfiles=Dataset(config['INPUT']['input_wrf'])
            
        self.Z = getvar(self.ncfiles, 'z',timeidx=ALL_TIMES, method="cat")
        self.U = getvar(self.ncfiles, 'ua',timeidx=ALL_TIMES, method="cat")
        self.V = getvar(self.ncfiles, 'va',timeidx=ALL_TIMES, method="cat")
        self.W = getvar(self.ncfiles, 'wa',timeidx=ALL_TIMES, method="cat")

        self.xlat = getvar(self.ncfiles[0], 'XLAT')
        self.xlon = getvar(self.ncfiles[0], 'XLONG')
        self.xh = getvar(self.ncfiles[0], 'HGT')
        self.final_t=strt_time+datetime.timedelta(hours=int(config['CORE']['integration_length']))

        print(print_prefix+'init multi files successfully!')

if __name__ == "__main__":
    pass
