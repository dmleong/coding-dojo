# Create a function called 'multiply()' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

# Modify this function so that you can pass an additional argument to this function. The function should multiply each value in the array by this additional argument (call this additional argument 'factor' inside the function). For example say a = [2,4,10,16]. When you say

# b = multiply(a, 5);  
# print(b);
# this should print b which contains [10, 20, 50, 80 ].

def multiply(list,multiplier):
	newList = []
	for item in list: 
		item = item * multiplier
		newList.append(item)
	return newList
		
a = [2, 4, 10, 16]
b = multiply(a,5)
print(b);