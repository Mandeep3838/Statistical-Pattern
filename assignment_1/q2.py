import numpy

'''
    Experiment performed 10000 times
 ''' 

x = numpy.zeros((10000,2))
y = numpy.zeros((10000,3))
z = numpy.zeros((10000,5))


'''
    Convert this problem from 2-D to 1-D representation
    Each point in 2-D mapped to a line segment 0 to 2*pi
    Random selections of points from the circumference
''' 
for i in range(10000):
    x[i] = numpy.random.uniform(0,2*numpy.pi,2)
    y[i] = numpy.random.uniform(0,2*numpy.pi,3)
    z[i] = numpy.random.uniform(0,2*numpy.pi,5)


'''
    Store number of successful experiments
'''
count_2_yes = 0
count_3_yes = 0
count_5_yes = 0


'''
    For n=2
    Strategy used 
    Distance between 2 points should be less than pi
 '''

for i in range(10000):
    if (max(x[i]) - min (x[i]) <= numpy.pi) or  2*numpy.pi - max(x[i]) + min(x[i]) <= numpy.pi:
        count_2_yes+=1


'''
    For n=3
    Strategy used
    1. Make a semicircle with each point as a starting point
    2. Identify the endpoints of the semicircle with that point 
    3. Check if other points lie within these end points
    4. If atleast 1 point satisfies Step 2 and 3, then semicircle is possible
        containing all points  
 '''
for i in range(10000):
    valid_semi_circle = False
    for j in range(3):
        end_point = []
        count = 0
        if y[i][j] <= numpy.pi:
            end_point.append(y[i][j] + numpy.pi)
        else:
            end_point.append(2*numpy.pi)
            end_point.append(y[i][j] - numpy.pi)
        for k in range(3):
            if len(end_point) == 1:
                if y[i][k] >= y[i][j] and y[i][k] <= end_point[0]:
                    count+=1
            else:
                if (y[i][k] >= y[i][j] and y[i][k] <= end_point[0]) or (y[i][k] >=0 and y[i][k] <= end_point[1]):
                    count+=1
        if count == 3:
            valid_semi_circle = True
    if valid_semi_circle:
        count_3_yes+=1 

        
'''
    For n=5
    Strategy used
    1. Make a semicircle with each point as a starting point
    2. Identify the endpoints of the semicircle with that point 
    3. Check if other points lie within these end points
    4. If atleast 1 point satisfies Step 2 and 3, then semicircle is possible
        containing all points  
 '''

for i in range(10000):
    valid_semi_circle = False
    for j in range(5):
        end_point = []
        count = 0
        if z[i][j] <= numpy.pi:
            end_point.append(z[i][j] + numpy.pi)
        else:
            end_point.append(2*numpy.pi)
            end_point.append(z[i][j] - numpy.pi)
        for k in range(5):
            if len(end_point) == 1:
                if z[i][k] >= z[i][j] and z[i][k] <= end_point[0]:
                    count+=1
            else:
                if (z[i][k] >= z[i][j] and z[i][k] <= end_point[0]) or (z[i][k] >=0 and z[i][k] <= end_point[1]):
                    count+=1
        if count == 5:
            valid_semi_circle = True
    if valid_semi_circle:
        count_5_yes+=1 


print("Probability for 2 points in a semi-circle", count_2_yes/10000)
print("Probability for 3 points in a semi-circle", count_3_yes/10000)
print("Probability for 5 points in a semi-circle", count_5_yes/10000)
