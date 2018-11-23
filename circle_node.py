# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 判断链表是否存在环
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        lst = []  # 用于存放节点
        p = pHead
        while p:
            if p in lst:
                return p  # 返回环的入口
            lst.append(p)
            p = p.next