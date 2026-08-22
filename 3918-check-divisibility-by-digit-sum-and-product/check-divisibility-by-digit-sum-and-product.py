import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        ans=[]
        for i in str(n):
            ans.append(int(i))
        res = sum(ans) + math.prod(ans)
        
        if n%res==0:
            return True 
        else:
            return False