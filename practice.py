# let's make two simple algorithms that finds the smallest and largest numbers in a list
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list3 = [1, 2, 100, 10, 2, 4, 8, 10]


def findSmallest(list):
    min = list[0]
    for number in list:
        if number < min:
            min = number
    return min


print(findSmallest(list1))
print(findSmallest(list2))
print(findSmallest(list3))


def findLargest(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    return max


print(findLargest(list1))
print(findLargest(list2))
print(findLargest(list3))
