def insert_sort(lst):
    """ 插入排序 """
    n = len(lst)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
            else:
                break


ss = [9, 8, 7, 6, 5, 4, 1]
insert_sort(ss)
print(ss)
