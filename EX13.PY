print("Dhanansezhiyan Computer Mark")
print("Nehur Street Paducheiry")
print("------------------------")
print("Bill Recpit")
print("------------")
no=int(input("Enter the Item No:"))
name=input("Enter the Particulares:")
rate=int(input("Enter the Rate:"))
quantity=int(input("Enter the Quantity:"))
total=rate*quantity
print("Total Amount in Pupees:",total)
if(total>=100000):
    gst=total*10/100
    print("gst:",gst)
elif(total>=50000):
    gst=total*5/100
    print("gst:",gst)
elif(total>=20000):
    gst=total*3/100
    print("gst:",gst)
else:
    gst=total*2/100
    print("Gst Good & Service Tax:",gst)
amt=total+gst
print("Amount to be Paid:",amt)
