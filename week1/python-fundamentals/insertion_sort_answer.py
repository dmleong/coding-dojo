# Insertion Sort
#Insertion Sort w/ While-Loop

x = [23,11,2,27,1,16]

def insertion_sort1(my_list):
    len_list = len(my_list)
    # loop through every element after the first
    for i in range(1,len_list):
        current = my_list[i]
        counter = i
        while counter > 0 and my_list[counter - 1] > current:
            my_list[counter] = my_list[counter-1]
            counter -= 1
        my_list[counter] = current
    return my_list

print insertion_sort1(x)

# Insertion Sort w/ nested For-Loop

x = [23,11,2,27,1,16]
def insertion_sort2(my_list):
    len_list = len(my_list)
    for i in range(1, len_list):
        temp = my_list[i]
        insert = i
        for j in range(0,i):
            if temp < my_list[i-1-j]:
                my_list[i - j] = my_list[i - 1 - j]
                insert = i - 1 - j

        if i != insert:
            my_list[insert] = temp
    return my_list

print insertion_sort2(x)
