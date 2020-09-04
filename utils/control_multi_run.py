#/usr/bin/env python
'''
Date: Sep 3, 2020

auto run

Zhenning LI

'''
import sys, os
import datetime
sys.path.append('../')
from lib.cfgparser import read_cfg, write_cfg

mo_lst=['01', '04', '07', '10']
ini_date=datetime.datetime.strptime('2016010112','%Y%m%d%H')
final_date=datetime.datetime.strptime('2016103012','%Y%m%d%H')

ini_delta=datetime.timedelta(days=3)
spinup_delta=datetime.timedelta(hours=24)

wrf_prefix='/home/dataop/data/nmodel/wrf_2doms_enlarged'
wrf_lst=[]
while ini_date <= final_date:

    yyyy=ini_date.strftime('%Y')
    yyyymm=ini_date.strftime('%Y%m')
    yyyymmddhh=ini_date.strftime('%Y%m%d%H')
    cal_time=ini_date+spinup_delta

    wrf_fn='wrfout_d01_'+cal_time.strftime('%Y-%m-%d_%H:%M:%S')
    if yyyymm[-2:] in mo_lst:
        wrf_lst.append(wrf_prefix+'/'+yyyy+'/'+yyyymm+'/'+yyyymmddhh+'/'+wrf_fn)
    ini_date=ini_date+ini_delta
for wrf_fn in wrf_lst:
    cfg_hdl=read_cfg('../conf/config.ini')
    cfg_hdl['INPUT']['input_wrf']=wrf_fn
    print(wrf_fn)
    write_cfg(cfg_hdl,'../conf/config.ini')
    os.system('cd ..; python run.py; cd utils')



