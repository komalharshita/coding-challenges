from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(names, heights))
        people.sort(key = lambda x : x[1], reverse = True)
        sortppl = [name for name, _ in people]
        return sortppl
