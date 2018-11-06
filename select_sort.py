def select_sort(lst):
    """ 选择排序 """
    n = len(lst)
    for j in range(n - 1):
        m = j
        for i in range(j+1, n):
            if lst[i] < lst[m]:
                m = i
        lst[m], lst[j] = lst[j], lst[m]


ss = [9, 8, 7, 6, 5, 4]
select_sort(ss)
print(ss)
