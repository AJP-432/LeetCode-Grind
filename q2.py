# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# Ajlal F. Paracha - Dec 13, 2022

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum = []
        carry = 0
        for v1, v2 in zip(l1, l2): 
            

            digit = v1 + v2 + carry 
            if digit > 9: 
                
                sum.append()


            else: sum.append(digit)
            
            














