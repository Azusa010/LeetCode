# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         result = []
#         seen = set()
#         for i in range(0, len(nums) - 2):
#             for j in range(i + 1, len(nums) - 1):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         temp = sorted([nums[i], nums[j], nums[k]])
#                         key = tuple(temp)
#                         if key not in seen:
#                             seen.add(key)
#                             result.append(temp)
#         return result


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        i = 0
        ans = []
        if(nums is None or len(nums)<3):
            return ans
        nums.sort()
        for i in range(0,len(nums)):
            left, right = i + 1, len(nums) - 1
            if nums[i] >0:
                break
            if nums[i] == nums[i-1] and i>0:
                continue
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                if s ==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    while(left<right and nums[left] == nums[left+1]):
                        left+=1
                    while(left<right and nums[right]==nums[right-1]):
                        right-=1
                    left+=1
                    right-=1
                elif s > 0:
                    right-=1
                elif s<0:
                    left+=1
        return ans

nums = [0,0,0]
print(Solution().threeSum(nums))
