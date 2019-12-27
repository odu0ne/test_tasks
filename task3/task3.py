import sys

data = [[]*16]*5

for i in range(1, 6):
    folder = sys.argv[1]
    with open(folder + 'Cash' + str(i) + '.txt') as inf:
        data[i-1] = [line.strip('\n') for line in inf]

summ = []
cash = []
for j in range(16):
    for i in range(len(data)):
        cash.append(float(data[i][j]))
    summ.append(sum(cash))
    cash = []
       
       
ind = summ.index(max(summ))


print(ind+1)