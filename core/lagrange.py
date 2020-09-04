#/usr/bin/env python
"""CORE: March the Air Parcel by Lagrangian Approach"""

import configparser
import datetime, math
import numpy as np

print_prefix='core.lagrange>>'

# CONSTANT
R_EARTH=6371000
DIS2LAT=180/(math.pi*R_EARTH)        #Distance to Latitude
CONST={'a':R_EARTH,'dis2lat':DIS2LAT}

def get_closest_idx_xy(lat2d, lon2d, airp):
    """
        Find the nearest x,y in lat2d and lon2d for lat0 and lon0
    """
    dis_lat2d=lat2d-airp.lat[-1]
    dis_lon2d=lon2d-airp.lon[-1]
    dis=abs(dis_lat2d)+abs(dis_lon2d)
    idx=np.argwhere(dis==dis.min())[0].tolist() # x, y position
    airp.ix.append(idx[0])    
    airp.iy.append(idx[1])    

def get_closest_idx_z(z3d, airp):
    """
        Find the nearest z in z3d 
    """
    
    h0=airp.h[-1]
    ix=airp.ix
    iy=airp.iy

    col_z=z3d[:,ix,iy]
    dis=abs(h0-col_z)
    airp.iz.append(np.argwhere(dis==dis.min())[0].tolist()[0]) # x, y position


def resolve_curr_xyz(airp, lat2d, lon2d, z3d):
    """
    Resolve air parcel location ( h, lat, lon) to (idx_t,idx_z,idx_lat,idx_lon)

    INPUT
    ---------
    """
    get_closest_idx_xy(lat2d, lon2d, airp)
    get_closest_idx_z(z3d, airp)
    
    
   
   
def lagrange_march(airp, u1d, v1d, w1d, dts):
    """
    March the air parcel (single) in the UVW fields
    """

    dx=u1d*dts
    dlon=dx*180/(CONST['a']*math.sin(math.pi/2-math.radians(airp.lat[-1]))*math.pi)
    
    dy=v1d*dts
    dlat=dy*CONST['dis2lat']
    
    dz=w1d*dts

    curr_t = airp.t[-1]+airp.dt

    airp.update(airp.lat[-1]+dlat, airp.lon[-1]+dlon, airp.h[-1]+dz, curr_t)
if __name__ == "__main__":
    pass
