# class Solution:
#     def subarraySum(self, nums: list[int], k: int) -> int:
#         count=0
#         for end in range(len(nums)):
#             sums= 0
#             for start in range(end,-1,-1):
#                 sums+=nums[start]
#                 if sums == k:
#                     count+=1
#         return count

"""
哈希表

数据结构:
mp(哈希表/字典): 存放前缀和，与出现次数
nn(当前前缀和)



想要找到和为k的子数组，使用前缀和的方法
求出列表每一个位置的前缀和，然后在存到前缀和表中，每次在表中查找 当前 n = 前缀和 - 目标k 的值是否在表中
如果在表中，就给结果加上 n 的 value也就是出现的次数
因为我们直到当前数的前缀和等于他前一个数字的前缀和+当前数字
由此可知当前数到他前面任意一个数的前缀和之差就是他们之间子数组的和

【为什么是 count += mp[nn-k]？】
因为 (nn - k) 这个值可能在之前出现过多次（比如数组中有 0 或负数），
每出现一次，就代表一个不同的起始位置，都能与当前位置组成一个有效的子数组。
所以要一次性加上出现的次数，而不是只加 1。

【为什么 mp 要初始化为 {0: 1}？】
为了处理子数组从下标 0 开始的情况。
如果整个数组的前缀和正好等于 k，那么 nn - k = 0，
此时需要在 mp 中找到 0，才能正确计数。
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        mp = {0:1}
        nn = 0
        for num in nums:
            nn += num
            if nn-k in mp:
                count+=mp[nn-k]
            mp[nn] = mp.get(nn,0)+1
        return count

nums = [1, 2, 3]
k = 3
print(Solution().subarraySum(nums, k))
