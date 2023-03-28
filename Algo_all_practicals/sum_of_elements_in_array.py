## practical 1(a)
lst=[]
num=int(input("Enter the size of array : "))
print("Enter array element")
for n in range(num):
   number=int(input())
   lst.append(number)
print("sum:",sum(lst))