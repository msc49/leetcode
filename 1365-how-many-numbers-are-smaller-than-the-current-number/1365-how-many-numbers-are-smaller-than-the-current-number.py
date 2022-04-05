class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = sorted(nums)
        results = []
        hash = {}
        
        for i in range(len(l)):
            if l[i] not in hash:
                hash[l[i]] = i
        
        for i in range(len(nums)):
            results.append(hash[nums[i]])
        return results