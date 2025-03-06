def linear(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [3,5,2,8,9,11]
x = 11
result = linear(arr, x)
if result != -1:
    print(f'find {x} in place {result+1}')
elif result == -1:
    print('not find this number')


print('-------------------------------------------------------')

def dodoyi(arr, x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

arr=[3,5,9,6,8,1,15,11]
arr.sort()
x=11
result = dodoyi(arr, x)
if result != -1:
    print(f'find {x} in place {result+1}')
elif result == -1:
    print('not find this number')








