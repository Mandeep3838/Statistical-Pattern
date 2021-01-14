import numpy

x = numpy.zeros((10000,2))
y = numpy.zeros((10000,3))
z = numpy.zeros((10000,5))

# Experiment performed 10000 times
for i in range(10000):
    x[i] = numpy.random.uniform(0,2*numpy.pi,2)
    y[i] = numpy.random.uniform(0,2*numpy.pi,3)
    z[i] = numpy.random.uniform(0,2*numpy.pi,5)

count_2_yes = 0
count_3_yes = 0
count_5_yes = 0

## Let semicircle is from 0 to pi
# Compute probability
for i in range(10000):
    if (x[i] < numpy.pi).all():
        count_2_yes+=1
    if (y[i] < numpy.pi).all():
        count_3_yes+=1
    if (z[i] < numpy.pi).all():
        count_5_yes+=1
    

print("Probability for 2 points in a semi-circle", count_2_yes/10000)
print("Probability for 3 points in a semi-circle", count_3_yes/10000)
print("Probability for 5 points in a semi-circle", count_5_yes/10000)
