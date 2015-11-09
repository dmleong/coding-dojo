import random
import datetime

t_start = datetime.datetime.now()

def selectionSort(arr): 
	#Single selection sort
	# counter = 0
	# for i in range(0, len(arr) - 1): 
	# 	minPos = i
		
	# 	# Linear scan to get min
	# 	for j in range(i + 1, len(arr)):
	# 		if arr[j] < arr[minPos]: 
	# 			minPos = j
	# 			counter += 1
		
	# 	temp = arr[minPos]
	# 	arr[minPos] = arr[i]
	# 	arr[i] = temp

	# print "Number of times if statement called" , counter

	#Come back to double selection sort
	for i in range(0, len(arr)/2): 
		minPos = i
		maxPos = i
		counter = 0

		for j in range(i + 1, len(arr) - counter): 
			print "j", arr[j]
			if arr[j] < arr[minPos]: 
				minPos = j

			if arr[j] > arr[maxPos]: 
				maxPos = j

		counter += 1
		# arr[minPos], arr[maxPos] = arr[maxPos], arr[minPos]

		print "Min", arr[minPos], "Max", arr[maxPos]



	# for i in range(0, len(arr) - 1):
	# 	for j in range(i, len(arr) - i - 1):
	# 		minIndex = j
	# 		maxIndex = arr[len(arr) - 1 - j]

	# 		minPos = arr.index(min(arr))
	# 		arr.insert(minIndex, arr.pop(minPos))

	# 		maxPos = arr.index(max(arr))
	# 		arr.insert(maxIndex, max(arr))
	# 		arr.remove(arr[maxPos])

	# 		print arr


# arr = random.sample(range(0, 10000), 100)
arr = [44, 3, 1, 2, 55, 11, 64, 34]
selectionSort(arr)
print(arr)

t_end = datetime.datetime.now()
runtime = t_end - t_start
print runtime