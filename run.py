"""
1. Set up the temperature for NPT calculation.
2. Run NPT calculation with LAMMPS
3. Extract the lattice parameters from log.lammps
4. Get the average of the lattice parameters.
5. Plot T vs a
"""

import os
import subprocess
import re
import numpy as np
import matplotlib.pyplot as plt

# Change this accordingly.
exe = "lmp_serial"
infile = "Pd.in"
outfile = "output.txt"
runtime = 100000
temperature = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 
               1250, 1500, 1750, 2000, 2500, 3000, 3500, 4000]
os.chdir("Pd/")

###############################################################################

lattices = []
for temp in temperature:
    os.mkdir(f'out_{temp}')
    
    # Step 1
    string_of_text = []
    with open(infile) as f:
        for line in f:
            if line[:17] == 'variable T equal ':
                line = line[:17]+f'{temp}\n'
                string_of_text.append(line)
            elif line[:23] == 'variable runtime equal ':
                line = line[:23]+str(runtime)+'\n'
                string_of_text.append(line)
            else:
                string_of_text.append(line)

    with open(infile, 'w') as f:
        for line in string_of_text:
            f.write(line)
    
    # Step 2
    #outfile = f"log{temp}.lammps"
    p = subprocess.Popen([exe, '-in', infile], stdout=subprocess.PIPE)
    stdout = p.communicate()[0]
    rc = p.returncode
    if rc != 0:
        error_msg = 'LAMMPS exited with return code %d' % rc
        msg = stdout.decode("utf-8").split('\n')[:-1]
        try:
            error = [i for i, m in enumerate(msg)
                    if m.startswith('ERROR')][0]
            error_msg += ', '.join([e for e in msg[error:]])
        except:
            error_msg += msg[-1]
        print(error_msg)

    # Step 3
    flog = open("log.lammps")

    lat = []
    for i, line in enumerate(flog):
        if i > 71 and i <= 71+(runtime/100+1):
            arr = re.split(r'\s+', line)
            print(arr)
            a = float(arr[2])
            lat.append(a/5)
    
    flog.close()
    os.remove("log.lammps")

    # Step 4
    lattices.append(np.mean(lat))

output = []
for i in range(len(temperature)):
    output.append([temperature[i], lattices[i]])
np.savetxt(outfile, output, delimiter=' ')

# Step 5
plt.plot(temperature, lattices, 'g^')
plt.xlabel('T (K)')
plt.ylabel('a (A)')
os.chdir("../")
plt.show()
#plt.savefig('results/result.png')
