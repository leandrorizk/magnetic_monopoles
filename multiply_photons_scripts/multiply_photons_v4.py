import os
import sys
from tqdm import tqdm

FILENAME = sys.argv[1]

try:
    FACTOR = int(sys.argv[2])
except:
    FACTOR = 4689
    
# read, then rewrite

lines = ''

with open(FILENAME, 'r') as f:
    for line in tqdm(f, 'Multiplying GrOptics photons'):
        if line.startswith('P '):
            line *= FACTOR
        lines += line

with open(FILENAME, 'w') as f:
    f.write(lines)