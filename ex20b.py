print("prime number gweneration")
print("---------")
sn=int(input("enter the starting number"))
en=int(input("enter the ending"))
print("result")
count=0
for n in range(sn,en):
    for i in range(2,n):
        if(n%i)==0:
            count+=1
            if count==0:
             print(n)
            
