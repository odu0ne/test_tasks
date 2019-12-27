import sys


with open(sys.argv[1]) as infTop:
    top =[line.strip('\n') for line in infTop]

topCoordinate = []
for i in range(len(top)):
    topCoordinate += [top[i].split()] 
    
topX = []
topY = []
    
for i in range(len(topCoordinate)):
    topX.append(float(topCoordinate[i][0]))
    topY.append(float(topCoordinate[i][1]))
        
    
    
with open(sys.argv[2]) as infPoint:
    point =[line.strip('\n') for line in infPoint]
    
pointCoordinate = []
for i in range(len(point)):
    pointCoordinate += [point[i].split()]

pointX = []
pointY = []
    
for i in range(len(pointCoordinate)):
    pointX.append(float(pointCoordinate[i][0]))
    pointY.append(float(pointCoordinate[i][1]))

   
 


 
for i in range(len(pointCoordinate)):
    iteration = 0
    for j in range(len(topCoordinate)):
        #print(pointX[i], topX[j],'\n', pointY[i], topY[j])
        if pointX[i] == topX[j] and pointY[i] == topY[j]:
            print('0\n')
            break
        elif (topY[j-1] - topY[j]) != 0 and (topX[j-1]<pointX[i]<topX[j] or topY[j-1]<pointY[i]<topY[j]) and (pointX[i] == (topX[j-1] - topX[j]) * (pointY[i] - topY[j]) / (topY[j-1] - topY[j]) + topX[j]):
            print('1\n') 
            break
        elif (((topY[j]<pointY[i]<topY[j-1]) or (topY[j-1]<pointY[i]<topY[j])) and pointX[i] > (topX[j-1] - topX[j]) * (pointY[i] - topY[j]) / (topY[j-1] - topY[j]) + topX[j]):
            print('2\n')
            break
        
        
        if ((topY[j-1] - topY[j]) != 0 and (pointX[i] < (topX[j-1] - topX[j]) * (pointY[i] - topY[j]) / (topY[j-1] - topY[j]) + topX[j])) and (not(topY[j]<pointY[i]<topY[j-1]) or not(topY[j-1]<pointY[i]<topY[j]))\
              or (not(topY[j]<pointY[i]<topY[j-1]) or not(topY[j-1]<pointY[i]<topY[j])) and (not(topX[j]<pointX[i]<topX[j-1]) or not(topX[j-1]<pointX[i]<topX[j])):
            iteration +=1
            if iteration == len(topCoordinate):
                print('3\n')
