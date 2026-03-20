class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
solution = Solution()

lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
tgt = int(input("Enter the target number: "))

result = solution.twoSum(lst, tgt)
print(result)