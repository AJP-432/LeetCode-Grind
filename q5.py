# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# Ajlal F. Paracha - Dec 14, 2022

class Solution:
    def longestPalindrome(self, s: str) -> str:

        words, current_longest = [], ""
        
        for i in range(len(s)): 

            for word in words: 
                word += s[i]
                if word == word[::-1] and len(word) > len(current_longest): 
                    current_longest = word

            words.append(s[i])

        return current_longest