# Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
# Traverse through all array elements
    for i in range(n):
# Last i elements are already in place
        for j in range(0, n-i-1):
# traverse the array from 0 to n-i-1
# Swap if the element found is greater
# than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i],end=" ")
print('\n')
    





# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]
 # Traverse through all array elements
for i in range(len(A)):

 # Find the minimum element in remaining
 # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

 # Swap the found minimum element with
 # the first element
    A[i], A[min_idx] = A[min_idx], A[i]
 # Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i],end=" ")



# Function to do insertion sort
def insertionSort(arr):
 # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
 # Move elements of arr[0..i-1], that are
 # greater than key, to one position ahead
 # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    arr = [12, 11, 13, 5, 6]
print('\n')
print('Sorted array: ')
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i],end=' ')

    
#Bubble Sort:
#The time complexity of the bubble sort algorithm is O(n^2) because it uses nested loops to traverse the array, and the worst-case scenario occurs when the array is sorted in reverse order. The space complexity is O(1) because it only requires a temporary variable to swap elements.

#Selection Sort:
#The time complexity of the selection sort algorithm is O(n^2) because it uses nested loops to traverse the array, and the worst-case scenario occurs when the array is sorted in reverse order. The space complexity is O(1) because it only requires a temporary variable to swap elements.

#Insertion Sort:
#The time complexity of the insertion sort algorithm is O(n^2) because it uses nested loops to traverse the array, and the worst-case scenario occurs when the array is sorted in reverse order. The space complexity is O(1) because it only requires a temporary variable to swap elements.
