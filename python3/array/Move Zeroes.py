"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        o=nums.count(0)
        for t in range(o):
            for k in range(len(nums)):
                if nums[k]==0: 
                    nums.remove(nums[k])
                    nums.append('0')    