class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        
        if numbers is None or len(numbers) < 3 or numbers[0] > 0:
            return []
            
        res = []
        s = 0
        
        while s <= len(numbers) - 3:
            a = numbers[s]
            j = s + 1
            k = len(numbers) - 1
            while j < k:
                b = numbers[j]
                c = numbers[k]
                if a + b + c == 0:
                    res.append([a, b, c])
                    j += 1
                    k -= 1
                if a + b + c < 0:
                    j += 1
                if a + b + c > 0:
                    k -= 1
            s += 1
            
        res1 = []
        for i in res:
            if i not in res1:
                res1.append(i)
                
        return res1
        
        