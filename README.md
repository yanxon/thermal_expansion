# Thermal Expansion Calculation with LAMMPS

 Here, I provide an example of autamated thermal expansion calculations of periodic boundary condition fcc Palladium (Pd) using LAMMPS. 

Zhou et. al. EAM potential for PdH is used. Using LAMMPS, [NPT](https://lammps.sandia.gov/doc/fix_nh.html) method (constant number of particles, pressure, and temperature) will be performed.

I am using Python as scripting language to prepare for the automation of NPT calculations at different temperatures. 

## Dependencies
- Python
- [LAMMPS](https://github.com/lammps/lammps)

## Execute
To run, please execute this command:
```
python run.py
```

## Result

![image](https://github.com/yanxon/thermal_expansion/blob/master/results/Pd.png)
