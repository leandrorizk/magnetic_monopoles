import os
import sys
from tqdm import tqdm

try:
    FACTOR = int(sys.argv[1])
except:
    FACTOR = 11
    
files = [f for f in os.listdir() if f.startswith('photons')]
data_file = files[0]

# read and write

f_read = open(data_file, 'r')
f_write = open('multiplied.dat', 'w')

for line in tqdm(f_read):
    if line.startswith('P '):
        line *= FACTOR
    f_write.write(line)

f_read.close()
f_write.close()