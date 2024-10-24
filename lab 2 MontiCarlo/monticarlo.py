'''
To find the vlaue if pi using monticarlo method
Assume a unit circle of at the center at origin then range in both x and y 
axis is -1 to 1. Then 
    x**2 + y**2=1
or  y=sqrt(1-x**2)

integratation(-1,1)(y)dx=pi/2

we know in monticarlo 
area undeer the curve / area of recatngle 
                    =
# of points under the curve / # of points inside the rectangle

or    I/c*(b-a) = n/N
or    I=  c*(b-a)*n/N
or    pi/2= c*(b-a)*n/N
      pi = 2* c*(b-a)*n/N

to  find n we randonly genreate x and y using random.uniform() and check if it is 
under of above the curve
i.e. is   y <= sqrt(1-x**2)
    if yes => n++
'''
import random
import math

def f(x):
    return math.sqrt(1-x**2)
while(1):

    xUpperLimit=1
    xLowerLimit=-1
    yUpperLimit=1
    yLowerLimit=0
    underCurveCount=0

    totalCount = int(input("enter number of points "))

    for i in range(totalCount):
        x=random.uniform(xLowerLimit,xUpperLimit)
        y=random.uniform(yLowerLimit,yUpperLimit)
        #print(i,x,y)
        if y <= f(x):
            underCurveCount+=1
            #print("accepted")
        #else:
            #print("denied")
        
    valueOfPi = 2 * yUpperLimit *(xUpperLimit-xLowerLimit)* underCurveCount / totalCount

    print("The calculated value of pi is ",valueOfPi)
    error = abs(valueOfPi - math.pi)*100 / math.pi
    print("error %  = ", error)
    fhfh = input()    



