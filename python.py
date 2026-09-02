a=10
b=3
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)
print("floor division:",a//b)
print("remainder:",a%b)
print("power:",a**b)


#simple calculator
a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
print("addition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)
print("division:",a/b)

#student marks calculator
name= input("Enter student name:")
m1= int(input("Enter python marks:"))
m2= int(input("Enter java marks:"))
m3= int(input("Enter sql marks:"))

total= m1+m2+m3
average= total/3

print("\n----Student Marks Report----")
print("name:",name)
print("total marks:",total)
print("average marks:",average)

#shopping bill calculator
price1= float(input("Enter price of item 1:"))
price2= float(input("Enter price of item 2:"))
price3= float(input("Enter price of item 3:"))
total_price= price1+price2+price3
discount:float= total_price*0.10
final_price= total_price-discount

