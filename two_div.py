def two_div(lst, val):
    """ 二分法查找 """
    # 递归法
    n = len(lst)
    if n == 0:
        return False
    else:
        mid = n // 2
        if lst[mid] == val:
            return True
        elif lst[mid] > val:
            return two_div(lst[:mid], val)
        elif lst[mid] < val:
            return two_div(lst[mid+1:], val)
        else:
            return False


def two_div1(lst, item):
    # 非递归
    n = len(lst)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == item:
            return True
        if lst[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return False


ss = [1, 4, 5, 6, 7, 8, 9]
print(two_div(ss, 0))
print(two_div(ss, 1))
