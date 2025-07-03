#Question: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

#Solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen = {}
        for i in range(len(nums)):
            seen[nums[i]] = i
        
        nums1 = list(seen.keys())
        nums.clear()

        nums += nums1
        
        return(len(nums))


#Following code could have worked but the set() function pushed all negative values to the end of the set:

   #nums_set = set(nums)
   #nums.clear()

   #nums += list(nums_set)
