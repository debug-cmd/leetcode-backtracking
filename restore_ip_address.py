class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        left, idx = 0, 0
        currArr = ["", "", "", ""]
        self.backtrack(s, len(s), currArr, result, left, idx)
        
        return list(map(lambda x: ".".join(x), result))
    
    def backtrack(self, s, n, currArr, result, left, idx):
        if left >= n or idx > 3:
            return
        
        if idx == 3:
            if int(s[left:]) > 255 or (s[left] == "0" and left+1 < n):
                return
            newArr = currArr.copy()
            newArr[idx] = s[left:]
            result.append(newArr)
        
        if s[left] == 0:
            newArr = currArr.copy()
            newArr[idx] = "0"
            self.backtrack(s, n, newArr, result, left+1, idx+1)
            
        for i in range(1, 4):
            if int(s[left:left+i]) <= 255:
                newArr = currArr.copy()
                if s[left] == "0":
                    if i == 1:
                        newArr[idx] = "0"
                        self.backtrack(s, n, newArr, result, left+1, idx+1)
                else:
                    newArr[idx] = s[left:left+i]
                    self.backtrack(s, n, newArr, result, left+i, idx+1)
