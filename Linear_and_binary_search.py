##linear Search practical_4(a)

def LinearSearch(array, n, k):
    for j in range(0, n):
        if (array[j] == k):
            return j
    return -1
array = [1, 3, 5, 7, 9]

k = 5
n = len(array)

result = LinearSearch(array, n, k)

if(result == -1):

    print('Element not found&quot')

else:
    print('Element found at index: ', result)


##Binary search(iterative) practical_4(b)

def binarySearch(arr, k, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 3, 5, 7, 9]
k = 5
result = binarySearch(arr, k, 0, len(arr)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")


##Binary search(recursive) practical_4(b)



def BinarySearch(arr, k, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return BinarySearch(arr, k, low, mid-1)
        else:
            return BinarySearch(arr, k, mid + 1, high)
    else:
        return -1
arr = [1, 3, 5, 7, 9]
k = 5
result = BinarySearch(arr, k, 0, len(arr)-1)
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
