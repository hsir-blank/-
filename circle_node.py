# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# �ж������Ƿ���ڻ�
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        lst = []  # ���ڴ�Žڵ�
        p = pHead
        while p:
            if p in lst:
                return p  # ���ػ������
            lst.append(p)
            p = p.next