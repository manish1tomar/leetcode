"""
Permutations
Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [7]

Output: [[7]]
Constraints:

1 <= nums. length <= 6
-10 <= nums[i] <= 10"""


class Solution:
    def permute(self, nums: [int]) -> [[int]]:
        if len(nums) == 0:
            return [[]]

        print("1")
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            print("2")
            for i in range(len(p)+1):
                print("3")
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
                print(p_copy)

        return res

s = Solution()
p = s.permute([1,2,3])
print(p)