# This program will find the greatest common divisor for two variables input by the user

# Define variables
dividend = 0    # dividend variable
divisor = 0     # divisor variable
remainder = 1   # remainder variable initialized to 1 in order to check for a remainder

# Instructions to the user
print("This program will find the greatest common divisor for two variables. \n")

input1 = raw_input("Enter your first variable: ")

input2 = raw_input("Enter your second variable: \n")

# The code puts the input variables into variables used in the division statement
# The larger of the two numbers must be the dividend
if input1 > input2:
    dividend = int(input1)
    divisor = int(input2)
else:
    dividend = int(input2)
    divisor = int(input1)

# Begin process to examine the remainder
# If the remainder is greater than zero, the divisor is moved to the dividend and the new dividend
# is divided by the remainder. This process repeats until the remainder is zero. Then, the last divisor is
# the greatest common divisor.

while remainder != 0:
    remainder = dividend % divisor
    if remainder != 0:
        dividend = divisor
        divisor = remainder

print("\nThe greatest common divisor for your variables is: " + str(divisor))
