"""
给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

样例
例如，对于给定的整数数组S=[1, 0, -1, 0, -2, 2] 和 target=0. 满足要求的四元组集合为：

(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)                                 
"""

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        numbers.sort()
        res = []
        
        for first in range(len(numbers) - 3):
            if first != 0 and numbers[first] == numbers[first - 1]:
                continue
            a = numbers[first]
            for second in range(first+1, len(numbers) - 2):
                if second != first + 1 and numbers[second] == numbers[second - 1]:
                    continue
                b = numbers[second]
                j = second + 1
                k = len(numbers) - 1
                while j < k:
                    c = numbers[j]
                    d = numbers[k]
                    if a + b + c + d == target:
                        res.append([a, b, c, d])
                        j += 1
                        k -= 1
                        while j < k and numbers[j] == numbers[j - 1]:
                            j += 1
                        while j < k and numbers[k] == numbers[k + 1]:
                            k -= 1
                    if a + b + c + d < target:
                        j += 1
                    if a + b + c + d > target:
                        k -= 1
        return res