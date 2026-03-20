class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        padded_nums = [str(num).zfill(4) for num in [num1, num2, num3]]
        key_digits = []

        for i in range(4):
            smallest_digit = min(int(padded_nums[0][i]), int(padded_nums[1][i]), int(padded_nums[2][i]))
            key_digits.append(str(smallest_digit))
    
        key = int(''.join(key_digits))
        return key