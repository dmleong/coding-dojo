# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.

# Sample output should be like the following:

#           Starting the program...

#           Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far

# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far 
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far 
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far 

# Ending the program, thank you!
# Here are some hints that might help:

# 1. Use the python random module to generate a random number

# import random
# random_num = random.random()
# # the random function will return a floating point number,
# # that is 0.0 <= random_num < 1.0
# 2. Use the python built-in round function to convert that floating point number into an integer

# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# # y_rounded will be rounded up to 1

import random 
def coinToss():
	head_count = 0;
	tail_count = 0;
	toss_count = 0;

	for x in range(1, 5001): 
		toss = round(random.random())
		if toss == 0:
			head_count += 1
			toss_count += 1
			print "Attempt #", toss_count , ": Throwing a coin... It's a head! ... Got " , head_count , "head(s) so far and " , tail_count , "tail(s) so far"
		else: 
			tail_count += 1
			toss_count += 1
			print "Attempt #", toss_count , ": Throwing a coin... It's a tail! ... Got " , head_count , "head(s) so far and " , tail_count , "tail(s) so far"

coinToss()