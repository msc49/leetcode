class Solution:
    def isHappy(self, n: int) -> bool:
        
        a = set()
        while n!= 1:
            if n  in a:
                return False
            
            a.add(n)
            n = sum([int(i) **2 for i in str(n)])
            
        return True
        