print('hello world')

def binarySearch(arry, x) :
    low = 0
    high = len(arry) - 1
    while low <= high :
        mid = int((low + high) / 2)
        guess = arry[mid]
        if guess == x :
            return mid
        if guess > x :
            high = mid - 1
        else :
            low = mid + 1
    return None


print(binarySearch([1,2,3,4,5,6,7], 5))