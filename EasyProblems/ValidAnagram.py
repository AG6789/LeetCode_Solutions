#Question: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag = False
        def strdict(s):
            sdict = {}
            for i in s:
                if i not in sdict:
                    sdict[i] = 1
                else:
                    sdict[i] += 1
            
            return sdict
        if len(s) == len(t):
            if strdict(s) == strdict(t):
                flag = True
        
        return flag





        
