class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        for i in range(n):
            total_pushes += self.calculate_push_cost(i)  # accumulate push cost per letter
        return total_pushes

    def calculate_push_cost(self, index: int) -> int:
        return index // 8 + 1  # 8 keys: position = index // 8 + 1