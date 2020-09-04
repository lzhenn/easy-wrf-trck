# Easy-WRF-Trck
Easy-WRF-Trck is a super lightweight Lagrangian model for calculating millions of WRF trajectories. 
It implements super simplified equations of 3-D motion to accelerate integration, and python multiprocessing is also involved to parallelize the model integration.
Due to its simplification and parallelization, Easy-WRF-Trck performs great speed in large-scale air mass tracing tasks, for example, calculating millions of mass points trajectories simultaneously.


**Caution: Trajectory calculation is based on the nearest-neighbor interpolation and first-guess velocity for super efficiency. Accurate calculation algorithm can be found on http://journals.ametsoc.org/doi/abs/10.1175/BAMS-D-14-00110.1**


### Input Files

`./input/input.csv` This file prescribe the mass points for trajectory calculations. The style of this file:

```
mass_id, init_lat, init_lon, init_h0 (m)
```

#### configure.ini
Configure file for the model. You may set WRF input file, input frequency, integration time steps and other settings in this file.

#### points.csv


### Module Files

### run.py
Main script to run the traj_model with multiple input files. 

