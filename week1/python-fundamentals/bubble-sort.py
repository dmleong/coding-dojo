import random
import datetime

tstart = datetime.datetime.now()

def bubbleSort(arr): 
	exchanges = True
	numrange = len(arr) - 1

	while numrange > 0 and exchanges: 
		exchanges = False
		for i in range(numrange): 
			if arr[i] > arr[i+1]: 
				exchanges = True
				(arr[i], arr[i+1]) = (arr[i+1], arr[i])
		numrange -= 1
	return arr
			

arr = random.sample(range(1, 10000), 100)
sorted = bubbleSort(arr)
print sorted

tend = datetime.datetime.now()
runtime = tend - tstart
print runtime