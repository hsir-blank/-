def quick_sort(lst, left, right):
    low = left
    high = right
    if left >= right:
        return
    key = lst[low]
    while low < high:
        while low < high and lst[high] >= key:
            high -= 1
        lst[low] = lst[high]
        while low < high and lst[low] <= key:
            low += 1
        lst[high] = lst[low]
    lst[low] = key
    quick_sort(lst, left, low - 1)
    quick_sort(lst, low + 1, right)


ss = [9, 8, 7, 6, 5, 4, 1]
quick_sort(ss, 0, len(ss)-1)
print(ss)
