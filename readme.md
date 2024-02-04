# Age Calculator Readme

## Description
This Python script takes the current year and your age as input and calculates the year you were born. It then determines whether you are an adult or a minor based on the calculated birth year.

## How to Use
1. Run the script by executing the provided code in a Python environment.
2. Enter the current year and your age when prompted.
3. The script will calculate and display the year you were born and determine if you are an adult or a minor.

## Script Explanation
The script uses the current year and your age to calculate your birth year. It then checks if you are 18 years or older to determine whether you are an adult or a minor.

```python
year = int(input("Please enter the current year: "))
age = int(input("Please enter your age: "))

birth_year = year - age 
print(f"You were born in the year {birth_year}")

if birth_year >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
