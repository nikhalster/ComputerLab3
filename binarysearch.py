#Kshitij Nikhal
#Binary Search for unsorted list

def acceptInput():
    unsorted = []
    n = int(input("Enter how many numbers to sort"))
    for i in range(0, n):
        unsorted.append(int(input()))
    print(unsorted)
    return unsorted, n

def bubbleSort(unsorted, n):
    for i in range(0,n):
        for j in range(i+1, n):
            if unsorted[j] < unsorted[i]:
                unsorted[j], unsorted[i] = unsorted[i], unsorted[j]
    return unsorted


def binarySearch(sort, find):
    mid = len(sort) / 2
    if mid == 0:
        print("Not found")
        return
    if find == sort[mid]:
        print("Found")

    if find < sort[mid]:
        binarySearch(sort[:mid], find)
    if find > sort[mid]:
        binarySearch(sort[mid+1:], find)


if __name__ == '__main__':
    unsorted, n = acceptInput()
    sort = bubbleSort(unsorted, n)
    find = int(input("Enter element to be searched"))
    binarySearch(sort, find)