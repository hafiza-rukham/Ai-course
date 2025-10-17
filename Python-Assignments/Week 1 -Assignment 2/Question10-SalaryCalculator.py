Basic_Salary=int(input("Enter the amount of Basic Salary:"))
HRA=(20/100)*Basic_Salary
DA=(15/100)*Basic_Salary
total_salary=HRA+DA+Basic_Salary
print("HRA 20% of basic:",(20/100)*Basic_Salary)
print("DA 20% of basic:",(15/100)*Basic_Salary)
print("total_salary:",HRA+DA+Basic_Salary)