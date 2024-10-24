#make compound intrest 

principle = int (input("enter principle " ))
time = int (input("enter time in years "))
rate = int(input("entere intrest rate "))

def compoundIntrest( p,t,r):
    intrest = float (p *(1+(r/100)**t))
    return intrest

amount = compoundIntrest(principle,time,rate)
print("the interest amount  ",amount)
