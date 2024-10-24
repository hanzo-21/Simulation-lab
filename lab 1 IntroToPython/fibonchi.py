def fibi (n):
    a=1;b=1;c=2
    i=0
    while(i<n):
        print(a)
        a=b
        b=c
        c=a+b
    
    fibi(10)

