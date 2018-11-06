def bubble_sort(lst):
    """ 冒泡排序 """
    n = len(lst)
    for j in range(n - 1):
        for i in range(n - 1 - j):
            if lst[i + 1] < lst[i]:
                lst[i + 1], lst[i] = lst[i], lst[i + 1]


ss = [9, 8, 7, 6, 5, 4]
bubble_sort(ss)
print(ss)
