print("prime number checking")
print("-----")
n=int(input("enter the number"))
print("result")
count=0
for i in range(2,n):
   if(n%i)==0:
    count++i
if count==0:
  print(n+"is a prime")
else:
  print(n+"is not a prime")
