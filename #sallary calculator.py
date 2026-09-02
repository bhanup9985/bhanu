#sallary calculator
basic_salary=float(input("enter ypur basic salary: "))
hra=basic_salary *0.20
da=basic_salary *0.10
gross_salary=basic_salary +hra+da

print("basic salary: ",basic_salary)
print("HRA: ",hra)
print("DA: ",da)
print("Gross salary: ",gross_salary)