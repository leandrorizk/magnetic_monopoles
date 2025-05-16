import os
import sys
from tqdm import tqdm

try:
    FACTOR = int(sys.argv[1])
except:
    FACTOR = 4700
    
files = [f for f in os.listdir() if f.startswith('photons')]
data_file = files[0]

# read, then write

f_read = open(data_file, 'r')
f_write = open('multiplied.dat', 'w')

lines = ''
for line in tqdm(f_read, 'Multiplying GrOptics photons'):
    if line.startswith('P '):
        line *= FACTOR
    lines += line

f_write.write(lines)

f_read.close()
f_write.close()