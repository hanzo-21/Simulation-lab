
#a=input("enter a number")
#print(a)
#b=int(a)+int(a)
#print(b)

name="narayan"
age=32
height=5.8
grades = [34,66,75,77,88]
print(grades[2])
print(grades[-1])

height = [34,66,75,77,88]
weight = [77,66,75,77,88]
rent=32

#print(grades is height) # why fasle 
#print(grades is weight)
#print(rent is age) 
#print(77 in grades)


print(grades ,len(grades))
grades.append(69)
print(grades ,type(grades))
#grades.pop(69) checek what error 
print(grades ,len(grades))

for i in grades:
    print("my marks is: ",i)

thisTupel = [ 1,2,3,'e','T','o']
print(thisTupel)
for i in thisTupel:
    print(i)



def fuunctionname():
    a=1
    b=1
    c=2
    n=10
    i=0
    while(i<n):
        print(a)
        a=b
        b=c
        c=a+b
        i+=1
    
fuunctionname()
#crete a compund interest