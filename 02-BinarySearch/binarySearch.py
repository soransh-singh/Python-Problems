def binary_search(arr, num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = int((low + high)/2)
        print(mid)
        guess = arr[mid]
        if(guess == num):
            return mid
        elif(guess > num):
            high = mid - 1
        else:
            low = mid + 1
    return "not Found"

if __name__ == '__main__':
    #print(binary_search([1, 2, 3, 4, 5, 6], 8))
    print(binary_search([1, 2, 3, 4, 5, 6], 2))
