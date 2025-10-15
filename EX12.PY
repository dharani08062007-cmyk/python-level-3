print("Govenment of Tamilnadu")
print("Elertcity Board")
print("---------------")
print("Bill Recipt")
print("-----------")
no=int(input("Enter the EB.No:"))
n=input("Enter the Customer Name:")
pu=int(input("Enter the pruious Unit:"))
cu=int(input("Enter the Current Unit:"))
unit=cu-pu
print("Unit Conusmed",unit)
if(unit>=1000):
    amt=unit*10
    print("Amount to be Paid:",amt)
elif(unit>=500):
        amt=unit*5
        print("Emount to be Paid:",amt)
elif(unit>100):
    amt=unit*2
    print("Amount to be Paid:",amt)
else:
    print("Amount to be Paid",nil)
