#subscription level question
#solved on my own

nums1 = list(map(int, input("Enter first array: ").split()))
nums2 = list(map(int, input("Enter second array: ").split()))

print(nums1)
print(nums2)

nums1.sort()
nums2.sort(reverse= True)

result = sum(a*b for a, b in zip(nums1, nums2))
print("Minimum product sum = ", result)