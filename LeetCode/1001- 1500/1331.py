class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Build the value-to-rank mapping from sorted unique elements
        rank_map = self.buildRankMap(arr)
        return self.transformArray(arr, rank_map)

    def buildRankMap(self, arr: List[int]) -> dict:
        # Deduplicate and sort to establish rank order
        sorted_unique = sorted(set(arr))
    
        return {val: rank for rank, val in enumerate(sorted_unique, start=1)}

    def transformArray(self, arr: List[int], rank_map: dict) -> List[int]:
        return [rank_map[val] for val in arr]