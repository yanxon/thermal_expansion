import subprocess

exe = "lmp_daily"
in_file = "big_hybrid.in"

temperature = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1250, 1500, 1750, 2000]

for temp in temperature[:1]:
    string_of_text = []
    with open(in_file) as f:
        for line in f:
            if line[:17] == 'variable T equal ':
                line = line[:17]+f'{temp}\n'
                string_of_text.append(line)
            else:
                string_of_text.append(line)

    with open(in_file, 'w') as f:
        for line in string_of_text:
            f.write(line)
    
    outfile = f"log{temp}.lammps"
    p = subprocess.Popen([exe, '-in', in_file], stdout=subprocess.PIPE)
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
