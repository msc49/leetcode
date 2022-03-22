class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        b = str(x)[::-1]
        
        if y == b:
            return True
        else:
        
            return False