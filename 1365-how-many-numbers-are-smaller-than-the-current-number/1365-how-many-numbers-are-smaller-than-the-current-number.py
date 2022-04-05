class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j] < nums[i]:
                    arr[i] += 1
                elif nums[j] > nums[i]:
                    arr[j] += 1
        return arr