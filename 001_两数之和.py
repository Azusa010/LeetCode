# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         cur = 0

#         while cur < len(nums):
#             next = cur + 1
#             for index, item in enumerate(nums[next:]):
#                 sum = nums[cur] + item
#                 if sum == target :
#                     return [cur, index + next]
#             cur += 1


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return 


print(Solution().twoSum([3, 3], 6))
print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([2, 5, 5, 11], 10))
