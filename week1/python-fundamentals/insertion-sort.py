import random
import datetime

t_start = datetime.datetime.now()
def insertSort(arr): 
	for i in range(1, len(arr)):
		insert = i
		temp = arr[i]
		for k in range(0, i): 
			if temp < arr[i - 1 - k]: 
				arr[i - k] = arr[i - 1 - k]
				insert = i - 1 - k
		if insert != i:
			arr[insert] = temp
	print arr


arr = random.sample(range(1, 10000), 100)
insertion = insertSort(arr)
print insertion	

t_end = datetime.datetime.now()
runtime = t_end - t_start
print runtime