year = int(input("Please current year"))
age = int(input("Please enter your age"))

cal =  year - age 
print(f"You were born In the year {cal} ")
# f string to read input

if cal >= 18:
 print("you are an adult")
else:
 print("you are an minor")
