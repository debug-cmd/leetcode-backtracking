class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        excep = set()
        
        self.backtrack(nums, n, excep, [], result)
        
        return result
    
    
    def backtrack(self, nums, n, excep, currArr, result):
        
        if len(currArr) == n:
            result.append(currArr)
        
        for i in nums:
            if i in excep:
                continue
                
            newArr = currArr.copy()
            newArr.append(i)
            
            newExcep = excep.copy()
            newExcep.add(i)
            
            self.backtrack(nums, n, newExcep, newArr, result)
