"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        save={}

        for i,n in enumerate(nums):
            difference=target-n
            if difference in save:
                return [save[difference], i]
            save[n]=i
        return

if __name__=="__main__":
    sol=Solution()
    # Test Example 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Op:{sol.twoSum(nums1, target1)}")