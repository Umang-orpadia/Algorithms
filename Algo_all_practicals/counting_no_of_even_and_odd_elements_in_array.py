def CountEvenOdd(lst,arr_size):
   even_count=0
   odd_count=0
   for i in range(arr_size):
       if(lst[i]%2==0):
           even_count+=1
       else:
           odd_count +=1
   print("No of even elements: ",even_count)
   print("No of odd elements: ",odd_count)
lst=[]
num=int(input("Enter the size of array : "))
print("Enter array elements: ")
for i in range(num):
   numbers=int(input())
   lst.append(numbers)
n=len(lst)
CountEvenOdd(lst,n)