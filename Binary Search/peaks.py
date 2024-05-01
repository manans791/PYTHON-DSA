# Write a program to find peak in an array there can be multiple peaks hence do it accordingly

a= [0,1,2,3,4,5,4,3,2,1]

def peak_check(a):
    lo = 0
    hi = len(a) - 1

    while lo <= hi:
        mid = (lo+hi)//2
        mid_number = a[mid]

        if (mid == 0 or mid_number > a[mid - 1]) and (mid == len(a)-1 or mid_number >a[mid+1]):
            return mid
        elif a[mid+1] > mid_number:
            lo = mid + 1
        elif a[mid-1] > mid_number:
            hi = mid - 1
    return -1

print(peak_check(a))