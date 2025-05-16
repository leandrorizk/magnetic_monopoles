import os
import sys
from tqdm import tqdm

try:
    PATH = sys.argv[1]
except:
    PATH = './'

try:
    FACTOR = int(sys.argv[2])
except:
    FACTOR = 4700
    
files = [f for f in os.listdir(PATH) if f.startswith('photons')]

# read, then rewrite

for data_file in tqdm(files):
    
    lines = ''
    
    with open(data_file, 'r') as f:
        for line in tqdm(f, 'Multiplying GrOptics photons'):
            if line.startswith('P '):
                line *= FACTOR
            lines += line
    
    with open(data_file, 'w') as f:
        f.write(lines)