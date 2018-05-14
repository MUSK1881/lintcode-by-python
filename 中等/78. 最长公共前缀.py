"""
给k个字符串，求出他们的最长公共前缀(LCP)

样例
在 "ABCD" "ABEF" 和 "ACEF" 中,  LCP 为 "A"

在 "ABCDEFG", "ABCEFG", "ABCEFA" 中, LCP 为 "ABC"
"""

class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # write your code here
        res = ''
        if not strs:
            return res
        tmp = strs[0]
        for i in strs:
            if len(tmp) > len(i):
                tmp = i
        for i in range(len(tmp)):
            for j in range(len(strs)):
                if strs[j][i] != tmp[i]:
                    return res
            res += tmp[i]
        return res