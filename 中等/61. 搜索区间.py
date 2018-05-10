"""
给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。

如果目标值不在数组中，则返回[-1, -1]

样例
给出[5, 7, 7, 8, 8, 10]和目标值target=8,

返回[3, 4]

挑战
时间复杂度 O(log n)
"""

class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        res = []
        for i in range(len(A)):
            if A[i] == target:
                res.append(i)
        print(res)
        if res == []:
            return [-1, -1]
        elif len(res) == 1:
            return [res[0], res[0]]
        else:
            return [A[0], [-1]]