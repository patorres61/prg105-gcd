#This program will find the greatest common divisor for two variables input by the user

# #define variables

inpt1 = 0      # first user input variable
inpt2 = 0      # second user input variable
dvdnd = 0      # dividend variable
dvsr = 0       # divisor variable
rem = 1        # remainder variable

# Instructions to the user
print("This program will find the greatest common divisor for two variables. \n")
inpt1 = raw_input("Enter your first variable: ")
inpt2 = raw_input("Enter your second variable: \n")

# The code puts the input variables into variables used in the division statement
# The larger of the two numbers must be the dividend
if inpt1 > inpt2:
    dvdnd = int(inpt1)
    dvsr = int(inpt2)
else:
    dvdnd = int(inpt2)
    dvsr = int(inpt1)

# Begin process to examine the remainder
# If the remainder is greater than zero, the divisor is moved to the dividend and the new dividend
# is divided by the remainder. This process repeats until the remainder is zero. Then, the last divisor is
# the greatest common divisor.

while rem != 0:
    rem = dvdnd % dvsr
    if rem != 0:
        dvdnd = dvsr
        dvsr = rem

print("\nThe greatest common divisor for your variables is: " + str(dvsr))
