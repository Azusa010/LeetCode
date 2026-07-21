

"""
哈希表，滑动窗口

[数据结构]:
table(Counter/字典):统计字符串 p 中每个字符出现的次数
window(字典):统计滑动窗口中每个字符出现的次数
left(指针):窗口左边界
res(列表):存放符合结果的起始索引


想要找到字符串中所有字母异位词,可以用一个字典 window 来存窗口内的词 key 为 字符 , value 为 统计次数
可以引入Counter来统计可哈希的对象,如果某个键不存在Counter不会报错,直接返回0
左边界 left 默认为 0
遍历 字符串 s 的 索引,字符 
把遍历到的字符以及出现次数更新到window字典中
如果 这个 字符 不在 table 中,说明目前的window不是一个解，直接清空,并且把left移动到right+1
如果 当前window 中 这个 字符 在 window 的value(也是在窗口出现的次数) 大于 table中 这个字符出现的次数,就把左指针右移,直到window中
这个字符出现的次数不超过 table 中的value

如果 窗口window的长度等于字符串p的长度并且两个哈希表相同，就把left追加到res列表中
"""


from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s)<len(p):
            return []
        table = Counter(p)
        res=[]
        left = 0
        window = {}             
        for right,char in enumerate(s):
            window[char] = window.get(char,0)+1
            
            if char not in table:
                window.clear()
                left = right + 1
                continue
            while window.get(char,0) > table.get(char,0):
                left_chat = s[left]
                window[left_chat] -= 1
                if window[left_chat] == 0:
                    del window[left_chat]
                left += 1
            if right-left +1 == len(p) and window == table:
                res.append(left)
        return res
        
s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s,p))