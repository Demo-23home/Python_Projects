def binary_search(my_list, target):
    sorted_list = sorted(my_list)
    middle = 0
    start = 0
    end = len(my_list)
    steps = 0
    while start <= end:
        print(f"Steps:{steps}, {str(sorted_list[start:end+1])}")
        steps += 1
        middle = (start + end) // 2
        if target == sorted_list[middle]:
            return middle
        if target < sorted_list[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
binary_search(my_list, target)
