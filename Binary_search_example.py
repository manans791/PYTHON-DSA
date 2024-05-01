#W###rite a simple binary search to find the output value from an array the array is not sorted
#  you can do it

a = [1,2,4,5,1,2,3,55,66,44,1,5,25,13,14,14]
b = 13

a.sort()

def binary_search(a,b):
    lo = 0
    hi = len(a) -1

    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = a[mid]

        if mid_number == b:
            return mid
        elif mid_number < b:
            lo = mid + 1
        else:
            hi = mid - 1
    return "not Found"


print(binary_search(a,b))