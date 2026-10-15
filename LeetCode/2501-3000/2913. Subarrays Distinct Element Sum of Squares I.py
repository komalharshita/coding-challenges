class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        
        # Try every possible starting index
        for i in range(n):
            seen = set()
            # Expand the subarray one element at a time
            for j in range(i, n):
                seen.add(nums[j])
                total += len(seen) ** 2
                
        return total