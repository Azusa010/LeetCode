class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        lognest  = 0
        for x in numset:
            if x-1 in numset:
                continue
            y=x+1
            while y in numset:
                y+=1
            lognest=max(lognest,y-x)
        return lognest

nums = [0,3,7,2,5,8,4,6,0,1]
print(Solution().longestConsecutive(nums))

