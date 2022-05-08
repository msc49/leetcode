class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashNum = set()
        for i in nums:
            if i in hashNum:
                return True 
            else:
                hashNum.add(i)
        return False