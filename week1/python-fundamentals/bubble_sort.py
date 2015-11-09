# Bubble Sort

x = [10,2,65,8,1,7]

def bubble_sort(my_list):
    count = 0
    # create a flag to check to see if any swaps have been made
    swapped = True
    while swapped == True:
        # set our flag to false, if we don't make a swap in our loop
        # swapp will still be false so we know our list is sorted
        swapped = False
        # loop through one less element per time through the loop
        num_elements = len(my_list) - count - 1
        for i in range(num_elements): 
            # if two elements adjacent we compare them and swap if necessary
            if my_list[i] > my_list[i+1]:
                # we could swap like this
                # temp = my_list[i]
                # my_list[i] = my_list[i + 1]
                # my_list[i + 1] = temp
                # but we can do it in one line with tuple unpacking
                (my_list[i], my_list[i+1]) = (my_list[i+1], my_list[i])
                # if we made a swap then we can create a flag to continue looping
                swapped = True
    # return our sorted list
    return my_list

print bubble_sort(x)
