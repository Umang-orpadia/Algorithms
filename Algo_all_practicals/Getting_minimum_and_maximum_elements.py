
def getmin(lst, n):
    res = lst[0]
    for i in range(1, n):
        res = min(res, lst[i])
    return res

def getmax(lst, n):
    res = lst[0]
    for i in range(1, n):
        res = max(res, lst[i])
    return res

lst = []
num = int(input("Enter the size of array: "))
print("Enter array element : ")
for i in range(num):
    number = int(input())
    lst.append(number)
n = len(lst)
print("Minimum element of array:", getmin(lst, n))
print("Maximum element of the array:", getmax(lst, n))


