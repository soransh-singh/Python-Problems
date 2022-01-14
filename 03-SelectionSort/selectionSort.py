def find_smallest(arr):
    small_index = 0
    for i in range(1, len(arr)):
        if(arr[i] < arr[small_index]):
            small_index = i
    return small_index

def selection_sort(arr):
    for i in range(len(arr)):
        smallest = find_smallest(arr[i:])
        arr[i], arr[smallest + i] = arr[smallest + i], arr[i]
    return arr

if __name__ == '__main__':
    print(selection_sort([12, 34, 45, 43, 10, 9]))
    print(selection_sort([1, 3, 425, 143, 130, 439]))
