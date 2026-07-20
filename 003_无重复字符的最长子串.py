'''
滑动窗口
遍历字符串,如果i在列表li中,删除li中重复字符及以前的元素
if执行完后,无条件向li中追加 i ,
每次循环对比当前li长度和保存的最长的长度
'''


# class Solution:
#     def lengthOfLongestSubstring(self,s: str) -> int:
#         li = list()
#         res = 0
#         for i in s:
#             if i in li:
#                 idx = li.index(i)
#                 li = li[idx+1:]
#             li.append(i)
#             res = max(res,len(li))
#         return res


"""
哈希滑动窗口
遍历 字符串 的 索引和值，
如果 当前遍历的 char 在 窗口中出现过 ,就把左指针跳到重复字符的下一位
无论是否重复,都更新当前字符的最新索引(dic[char] = right)
每次遍历更新一次res

s="abcacb"
当第二次遇到a前:dic={"a":0,"b":1,"c":2}
第二次遇到a, a 在 dic中 并且 a 的value >= left 也就是0
左指针要跳转到重复字符的下一位 left = 0 + 1
继续执行,dic["a"] = 3
dic = {"a":3,"b":1,"c":2} 

"""

class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        dic = dict()
        res = 0
        left = 0
        for right,char in enumerate(s):
            if char in dic and dic[char]>=left:
                left = dic[char] + 1
            dic[char] = right
            res = max(res,right-left+1)
        return res

s="pwwkew"
print(Solution.lengthOfLongestSubstring(s,s))

#[a,b,c]