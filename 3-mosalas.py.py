

print (" enter a ,b ,c :\n")
a=int(input())
b=int(input())
c=int(input())

if a+b>c:
    if a+c>b:
        if b+c>a:
            print("it's a triangle ." )
            
else:
    print("it's not a triangle ")