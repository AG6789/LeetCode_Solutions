#Question: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#First Solution, Runtime 14 ms, Beats 57.19% of Solutions

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        nums_dict = {}
        for i in nums:
            if i not in (nums_dict):
                nums_dict[i] = 1
            else:
                flag = True
                break 
        
        return flag
