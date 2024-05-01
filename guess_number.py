# write a code where jack has to guess the number out of an array or list in the minimum times and he has to guess right

a=[10,9,8,7,6,5,4,3,2,1,0]
b=4

def guess_number(a,b):
    lo = 0
    hi = len(a) - 1

    while lo<=hi:
        mid = (lo+hi)//2     # finding the mid index
        mid_number = a[mid]   # assign variable to mid number

        if mid_number == b:
            return mid
        elif mid_number > b:     # if target number is in right
            lo = mid + 1
        elif mid_number < b:     # if target number is in left
            hi = mid - 1
    return 'Not found in array'

print(guess_number(a,b))