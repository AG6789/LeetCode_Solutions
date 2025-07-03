#Question: Given a string s, return true if it is a palindrome, or false otherwise.

#Solution:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for i in s:
            if i.isalnum():
                s_new+=i
        
        s_new = s_new.lower()
        return(s_new[::-1] == s_new)
