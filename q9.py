
# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/



class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)

        if num == num[::-1]: return True
        else: return False