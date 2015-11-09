# Create a program that counts from 1 to 2000. As it loops through each number, have your program generate the number and whether it's an odd number or whether it's an even number.

# Your program output should look like below

# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number

for item in range(1, 20001):
	if item % 2 != 0: 
		print "Number is", item, "This is an odd number."
	else:
		print "Number is", item, "This is an even number."