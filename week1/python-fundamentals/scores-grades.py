# Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what is the grade of that score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
# Result should be like this...

# Scores and Grades
# Score: 87; Your grade is B
# Score: 67; Your grade is D
# Score: 95; Your grade is A
# Score: 100; Your grade is A
# Score: 75; Your grade is C
# Score: 90; Your grade is A
# Score: 89; Your grade is B
# Score: 72; Your grade is C
# Score: 60; Your grade is D
# Score: 98; Your grade is A
# End of the program. Bye!

def scoreGrade():
	for count in range(0,11):
		data = raw_input("What is your score? ")
		try:
			score = int(data)
		except ValueError:
			print "Please insert a valid integer"
		else:
			if 60 <= score <= 69:
				print "Scores:", score , "; Your grade is D"
			elif 70 <= score <= 79:
				print "Scores:", score , "; Your grade is C"
			elif 80 <= score <= 89:
				print "Scores:", score , "; Your grade is B"
			elif 90 <= score <= 100: 
				print "Scores:", score , "; Your grade is A"
			elif score > 100: 
				print "You're an overachiever!"
			else: 
				print "You have failed"

	print "End of program. Bye!"

scoreGrade()