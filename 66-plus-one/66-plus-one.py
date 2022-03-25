class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = int(''.join(str(i) for i in digits))
        a += 1
        res = [int(i) for i in str(a)]
        return res