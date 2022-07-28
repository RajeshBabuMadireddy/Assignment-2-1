a=[(2,5),(1,2),(4,4),(2,3),(2,1)]
first=len(a)
for i in range(0,first):
    for j in range(0,first-i-1):
        if(a[j][-1]>a[j+1][-1]):
            temporary=a[j]
            a[j]=a[j+1]
            a[j+1]=temporary
print(a)            
