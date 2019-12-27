import math
import sys

with open(sys.argv[1]) as inf:
  x=[float(line.strip()) for line in inf]

def percentile(data, percentile):
  size = len(data)
  return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]

def find_average(x):
  return sum(x)/len(x)

print('%.2f'%percentile(x, 90),'\n%.2f' %percentile(x, 50),'\n%.2f' %max(x),'\n%.2f' %min(x),'\n%.2f' %find_average(x))
