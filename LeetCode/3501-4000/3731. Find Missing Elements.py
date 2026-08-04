class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        mini = min(nums)
        maxi = max(nums)
        frange = set(range(mini, maxi + 1))
        missing_elements = sorted(frange - set(nums))
        
        return missing_elements


# optimized solution

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        mini = min(nums)
        maxi = max(nums)
        num_set = set(nums)  
        missing_elements = [x for x in range(mini, maxi + 1) if x not in num_set] 
        
        return missing_elements