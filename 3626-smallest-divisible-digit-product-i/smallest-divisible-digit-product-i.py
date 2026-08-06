class Solution:
    def smallestNumber(self, n: int, t: int) -> int: 
        while True:
            ans = 1
            for i in str(n):
                ans*=int(i)
            if ans%t==0:
                return n
            n+=1

   