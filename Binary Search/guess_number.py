# write a code where jack has to guess the number out of an array or list in the minimum times and he has to guess right

a=[10,9,8,7,6,5,4,3,2,1,0]
b=4

def guess_number(a,b):
    lo = 0
    hi = len(a) - 1

    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = a[mid]

        if mid_number == b:
            return mid
        elif mid_number > b:
            lo = mid + 1
        elif mid_number < b:
            hi = mid - 1
    return 'Not found in array'

print(guess_number(a,b))