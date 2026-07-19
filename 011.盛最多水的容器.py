# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         maxA = 0
#         for i in range(len(height)):
#             for j in range(i+1,len(height)):
#                 curA = min(height[i],height[j]) * (j-i)
#                 if curA > maxA:
#                     maxA = curA
#         return maxA
#超时了

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left,right=0, len(height)-1
        maxA=0
        while left<right:
            width = right-left
            h = min(height[left],height[right])
            maxA = max(maxA,width*h)
            if height[left] < height[right]:
                left += 1
            else:
                right-=1
        return maxA
            

nums=[1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(nums))
