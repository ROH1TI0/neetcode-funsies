class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        while nums != []:
            maxCount = 0
            count = 0
            nums = sorted(nums)
            for i in range(len(nums)-1):
                if nums[i+1] - nums[i] == 1:
                    count += 1
                elif nums[i+1] - nums[i] == 0:
                    continue
                else:
                    maxCount = max(count, maxCount)
                    count = 0
            final = max(count, maxCount)
            return final + 1   
        return 0
        
            
