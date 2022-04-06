class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        hash = {}
        
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] += 1
        
        count = 0
        print(hash)
        for i in hash:
            if hash[i] == 1:
                count+=i
        return count