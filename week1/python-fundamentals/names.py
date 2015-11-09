# Create a program that prints  the following format (including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13

users = {
 'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def getNames(data, title): 
	print title
	for x in range(len(data)): 
		full_name = data[x]['first_name'] + " " + data[x]['last_name']
		print (x + 1), "-", full_name, "-", (len(full_name) - 1)

students = users['Students']
instructors = users['Instructors']

getNames(students, 'Students')
getNames(instructors, 'Instructors')