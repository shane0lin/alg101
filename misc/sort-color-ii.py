# https://www.jiuzhang.com/problems/info/143
# 给定一个有n个对象（包括k种不同的颜色，并按照1到k进行编号）的数组，将对象进行分类使相同颜色的对象相邻，并按照1,2，...k的顺序进行排序。
# 你可以返回答案任何一种正确的排列方式。
# 样例
# 给出数组[1, 2, 2, 3, 4, 4, 4, 1, 3]，一种答案为[1, 1, 2, 2, 3, 3, 4, 4, 4]。
# 输入: 
# [2,1,1,2,2] 
# 2
# 输出: 
# [1,1,2,2,2]

def sortColors2(self, colors, k):
    # write your code here
    if not colors:
        return colors
    self.sort(colors, 0, len(colors) - 1, 1, k)
    return colors
def sort(self, colors, start, end, color_from, color_to):
    if color_from == color_to:
        return
    color_mid = (color_from + color_to) // 2
    left, right = start, end
    while left <= right:
        while left <= right and colors[left] <= color_mid:
            left += 1
        while left <= right and colors[right] > color_mid:
            right -= 1
        if left <= right:
            colors[left], colors[right] = colors[right], colors[left]
            left += 1
            right -= 1
    self.sort(colors, start, right, color_from, color_mid)
    self.sort(colors, left, end, color_mid + 1, color_to)