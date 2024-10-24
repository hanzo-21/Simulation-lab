import datetime as dt

n = int(input('enter number of people'))
a=56
c=77
while(1):
    i=1
   
    num = [0]*n
    num[0]=n
    num[0]=(a*num[0]+c)%n

    while(i<n):
        num[i]=(a*num[i-1]+c)%n
        i+=1

    print(num) 