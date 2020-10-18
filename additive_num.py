class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        return self.backtrack(num, 0, len(num), [])
        
        
    def backtrack(self, num, left, n, currArr):
        
        if len(currArr) >= 3:
            if currArr[-1] != currArr[-2] + currArr[-3]:
                return False
            else:
                if left == n:
                    return True
        
        for i in range(left, n):
            newArr = currArr.copy()
            
            if num[left] == '0' and i != left:
                return False
            
            newArr.append(int(num[left:i+1]))
            if len(newArr) >= 3:
                if newArr[-1] != newArr[-2] + newArr[-3]:
                    continue
            res = self.backtrack(num, i+1, n, newArr)
            
            if res == True:
                return True
            
        
        
