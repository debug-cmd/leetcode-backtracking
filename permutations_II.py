class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        n = len(nums)
        excep = set()
        
        self.backtrack(nums, n, excep, [], result)
        
        return result
    
    def backtrack(self, nums, n, excep, currArr, result):
        if len(currArr) == n:
            result.append(currArr)
            return
        
        dupl = set()
        
        for i in range(n):
            if i in excep or nums[i] in dupl:
                continue
                
            newArr = currArr.copy()
            newArr.append(nums[i])
            
            newExcep = excep.copy()
            newExcep.add(i)
            dupl.add(nums[i])
            
            self.backtrack(nums, n, newExcep, newArr, result)
