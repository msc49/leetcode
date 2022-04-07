class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        frequency = {}
        
        for i in nums:
            if i not in frequency:
                frequency[i] = 1
            else:
                frequency[i] += 1
        for j in frequency:
            if frequency[j] == 1:
                return j