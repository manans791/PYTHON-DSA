# write a program to return index of array repeating the first repeat and the last time. return the index as well

a=[1,2,3,4,5,6,7,1,0,2,5,6,8,4,9,1,4,5,6,9]
b= 5

def first_occurence(a,b):
    lo = 0
    hi = len(a) - 1
    result = -1

    while lo<=hi:
        mid = (lo+hi)//2
        mid_number = a[mid]

        if mid_number == b:
            result = mid            #store the index in the variable
            hi = mid-1              # going left
        elif mid_number > b:
            hi = mid - 1
        else:
            lo = mid + 1
    print("First occurence index is",result)


def last_occurence(a, b):
    lo = 0
    hi = len(a) - 1
    result = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = a[mid]

        if mid_number == b:
            result = mid                #store the index in the variable
            lo = mid + 1                # going right
        elif mid_number > b:
            hi = mid - 1
        else:
            lo = mid + 1
    print("Last occurence index is",result)




(first_occurence(a, b))
(last_occurence(a, b))