#Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

#First Solution, O(n^2), takes care of all boundary conditions such as half values

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

       for i in nums:

        if target-i in nums and i != target/2:
            return([nums.index(i), nums.index(target-i)])
        
        elif i == target/2:

            index1 = nums.index(i)

            nums1 = [i for i in nums]
            nums1.pop(index1)

            if target/2 in nums1:
                index2 = (nums1.index(target/2) + 1)
                return [index1, index2]
            
            else:
                pass

        else:
            pass

#Optimal Solution (O(n)) - Didn't implement it myself but understood it for the future

#class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
#            map = {}
#            for i in range(0, len(nums)):
#                need = target - nums[i]
#                if need in map:
#                    return [map[need], i]
#                else:
#                    map[nums[i]] = i
#            return [-1, -1]
        
