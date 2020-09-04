# Easy-WRF-Trck
A Super Lightweight Backward trajectory calculation based on WRFOUT UVW

**Backward trajectory calculation is based on the linear interpolation and first-guess velocity for efficiency. Accurate calculation agrithm can be found in http://journals.ametsoc.org/doi/abs/10.1175/BAMS-D-14-00110.1**


### Input Files

#### configure.yml
Configure files for file path, integration length, and etc.

#### points.csv


### Module Files

### easy-wrf-trck.py
Main script to run the traj_model with multiple input files. 

### back_traj_model-multi-input-files.py 
Core calculation script with multiple input files. You can modify this file to utilize accurate algrithm.

### back_traj_model-one-input-file.py
Calculation script with only one input file (multiple timeframes).

