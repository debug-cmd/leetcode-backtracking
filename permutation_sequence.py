from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        self.length = 0
        self.idxx = k
        self.n = n
        self.excep = set()

        op = self.backtrack([], n)
                        
        return "".join(map(str, op))
    
    def backtrack(self, currArr, n, k):
        
        if k == self.idxx:            
            return currArr
            
            
        fact = factorial(n-1)
        val = (k-1)//fact

        self.excep.add(val+1)
        self.length += val*fact

        op = self.backtrack([], 1)
