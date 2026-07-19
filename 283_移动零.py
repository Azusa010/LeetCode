# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         cur = 0
#         last = len(nums) - 1
#         while cur < last:
#             if nums[cur] == 0:
#                 for i in range(cur,last):
#                     nums[i] = nums[i+1 ]
#                 nums[last] = 0
#                 last -= 1
#             else:
#                 cur+=1


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1


nums = [1,0,0]
#[1, 3, 12, 0, 0]
#[1, ]
Solution().moveZeroes(nums)
print(nums)
