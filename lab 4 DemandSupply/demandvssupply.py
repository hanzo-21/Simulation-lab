'''
demand and supply 
D = a+bP
S = c+dP
at equilibrium D=S

'''


import numpy as np
import matplotlib.pyplot as plt

#parameters of demand and supply
a=20
b=3
c=50
d=4


def Demand (P):
    return a-c*P

def Supply (P):
    return c+d*P


#range of price
P_span=(0,200)

plt.figure(figsize=(20,12))

plt.plot(P_span,Demand,label='Demand',color='b')
plt.plot(P_span,Supply,label='Supply',color='g')

eqb_price= (a-c)/(b+d)

eqb_quantity= a-b*eqb_price
plt.scatter(eqb_price,eqb_quantity,label='Equlibrium',color='r')

plt.title('Demand and supply')
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.legend()
plt.grid(True)
plt.show()

print(f'eqb price: {eqb_price:.2f}')
print(f'eqb Quantiry: {eqb_quantity:.2f}')






