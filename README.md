# Thermal Expansion Calculation with LAMMPS

This repo provides an example of autamated thermal expansion calculations of periodic boundary condition bcc Tungsten (W) using LAMMPS. 

Zhou et. al. EAM potential for W is used. LAMMPS will perform [NPT](https://lammps.sandia.gov/doc/fix_nh.html) method (constant number of particles, pressure, and temperature).

The python script is prepared to autamate NPT calculations at different temperatures. 

## Dependencies
Here are the software used:
- Python
- [LAMMPS](https://github.com/lammps/lammps)

## Execute
To run, please execute this command:
```
python run.py
```

## Result

![image](https://github.com/yanxon/thermal_expansion/blob/master/results/Pd.png)
