# let's make two simple algorithms that finds the smallest and largest numbers in a list
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list15 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
list3 = [1, 2, 100, 10, 2, 4, 8, 10]

# findSmallest finds the smallest number in a list
# list {list} - the list that you want to find the smallest number from
# return {number} - returns the smallest number in the list you passed in for the argument
def findSmallest(list):
    min = list[0]
    for number in list:
        if number < min:
            min = number
    return min


# testing the findSmallest function
print(findSmallest(list1))
print(findSmallest(list2))
print(findSmallest(list3))

# findLargest finds the largest number in a list
# list {list} - the list that you want to find the largest number from
# return {number} - returns the largest number in the list
def findLargest(list):
    max = list[0]
    for number in list:
        if number > max:
            max = number
    return max


# testing the findLargest function
print(findLargest(list1))
print(findLargest(list2))
print(findLargest(list3))

# sortList, as the name implies, sorts a numbered list, you can either sort it from greatest to least (descending) or least to greatest (ascending)
# list {list} - the numbered list you will pass into the function to be sorted
# format {string} - the valid options you can input for this parameter are "ascending" or "descending", depending on how you want to sort the list
# return {list} - the function will return the filtered list
def sortList(list, format):
    unfilteredList = list.copy()
    initialListLength = len(unfilteredList)
    filteredList = []
    if format == "descending":
        for cycles in range(0, initialListLength):
            max = unfilteredList[0]
            indexOfMax = 0
            for index in range(0, len(unfilteredList)):
                if unfilteredList[index] > max:
                    max = unfilteredList[index]
                    indexOfMax = index
            filteredList.append(max)
            unfilteredList.pop(indexOfMax)
        return filteredList
    if format == "ascending":
        for cycles in range(0, initialListLength):
            min = unfilteredList[0]
            indexOfMin = 0
            for index in range(0, len(unfilteredList)):
                if unfilteredList[index] < min:
                    min = unfilteredList[index]
                    indexOfMin = index
            filteredList.append(min)
            unfilteredList.pop(indexOfMin)
        return filteredList


print(sortList(list1, "descending"))
print(sortList(list1, "ascending"))
