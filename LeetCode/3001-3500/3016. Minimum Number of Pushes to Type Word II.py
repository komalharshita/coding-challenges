from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the frequency of each letter in the word
        freq_map = countFrequencies(word)
        # Sort frequencies in descending order (most frequent first)
        sorted_freqs = getSortedFrequencies(freq_map)
        # Greedily assign push costs and compute total pushes
        total = calculateTotalPushes(sorted_freqs)

        return total


def countFrequencies(word: str) -> dict:
    return Counter(word)

def getSortedFrequencies(freq_map: dict) -> list:
    return sorted(freq_map.values(), reverse=True)

def calculateTotalPushes(sorted_freqs: list) -> int:
    total_pushes = 0
    for i, freq in enumerate(sorted_freqs):
        push_cost = i // 8 + 1
        total_pushes += freq * push_cost
    return total_pushes