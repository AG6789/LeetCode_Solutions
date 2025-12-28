#Question: Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        sdict = {}
        ans = -1

        for i in s:
            if i not in sdict:
                sdict[i] = 1
            else:
                sdict[i] += 1

        for i in sdict:
            if sdict[i] == 1:
                ans = s.index(i)
                break
        
        return ans
                
        
