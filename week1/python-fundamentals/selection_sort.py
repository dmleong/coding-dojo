# Selection Sort

x = [23,4,12,1,31,14]

def selection_sort(my_list):
    # find the length of the list
    len_list = len(my_list)
    # loop through the values
    for i in range(len_list):
        # for each pass of the loop set the index of the minimum value
        min_index = i
        # compare the current value with all the remaining values in the array
        for j in range(i+1,len_list):
            # to update the min_index if we found a smaller int
            if my_list[j] < my_list[min_index]:
                min_index = j
        # if the index of the minimum value has changed
        # we will make a swap
        if min_index != i:
            # we could do the swap like this
            # temp = my_list[i]
            # my_list[i] = my_list[min_index]
            # my_list[min_index] = temp
            # but using tuple unpacking to swap values here makes it shorter
            (my_list[i], my_list[min_index]) = (my_list[min_index], my_list[i])
    # return our array
    return my_list

print selection_sort(x)
