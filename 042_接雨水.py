# class Solution:
#     def trap(self, height: list[int]) -> int:
#         res = 0
#         for i in range(len(height)):
#             if i == 0 or i == len(height)-1:
#                 continue
#             left_max = max(height[:i])
#             right_max = max(height[i+1:])
#             lower = min(left_max,right_max)
#             if lower > height[i]:
#                 res+=lower-height[i]
#         return res


"""
动态规划
由上一个方法知道，从左侧最高和右侧最高中选择较矮的一个，如果这个矮的大于当前遍历的列的高度，就做减法，并且加到结果上
由于每次都要重新获取一遍所有的高度,所以可以用两个列表max_left和max_right来代表每列的左侧最高和右侧最高
max_left[i]就是第i列左侧最高的墙,max_right[i]同理
可以用[0]*len(height)来初始化两个列表
获取左侧最高墙时候从1开始到len(height)-2结束,也就是range(1, len(height) - 1)
获得右侧最高墙的时候从列表尾开始遍历,一直遍历到索引0,就是range(len(height) - 2, -1, -1)
于0和len(height)-1的位置不会积水所以最后计算res的时候只需要range(1,len(height)-1)
range(start,end)的范围是[start,end)
"""


# class Solution:
#     def trap(self, height: list[int]) -> int:
#         if len(height) < 2:
#             return 0
#         res = 0
#         max_left = [0] * len(height)
#         max_right = [0] * len(height)
#         for i in range(1, len(height) - 1):
#             max_left[i] = max(height[i - 1], max_left[i - 1])
#         for i in range(len(height) - 2, -1, -1):
#             max_right[i] = max(height[i + 1], max_right[i + 1])
#         for i in range(1, len(height) - 1):
#             lower = min(max_left[i], max_right[i])
#             if lower > height[i]:
#                 res += lower - height[i]
#         return res

"""
栈
遍历height,如果当前指向的height[cur]>栈顶的height,出栈,并且计算当前cur墙和栈顶墙之前水的多少
通过:
    距离 = cur - 弹出后栈顶的索引值 - 1
    高度 类似左侧最高墙和右侧最高墙
         用其中较小的那一个高度,减去height[弹出的索引] 
    水 = 距离 * 高度
如果当前指向的height[cur]<=栈顶的height,入栈
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        res = 0
        stack = [] 
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom_idx = stack.pop()  
                if not stack:  
                    break
                left_idx = stack[-1]  
                width = i - left_idx - 1 
                h = min(height[left_idx], height[i]) - height[bottom_idx]  
                res += width * h
            stack.append(i) 
        return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height))
# [0,0,1,1,2,2,2,2,3,3,3,3]
