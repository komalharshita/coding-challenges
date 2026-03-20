class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = [nums[i] for i in range(1, len(nums), 2)]
        even = [nums[i] for i in range(0,len(nums), 2)]
        even.sort()
        odd.sort(reverse = True)
        res = []
        e = o = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even[e])
                e += 1
            else:
                res.append(odd[o])
                o += 1
        return res
        