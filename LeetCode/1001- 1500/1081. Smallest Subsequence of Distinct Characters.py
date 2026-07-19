class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = self.buildLastOccurrence(s)
        stk = []
        seen = set()
        for i, c in enumerate(s):
            if c in seen:
                continue
            while self.shouldPop(stk, c, i, last):
                seen.remove(stk.pop())
            stk.append(c)
            seen.add(c)
        return "".join(stk)

    def buildLastOccurrence(self, s: str) -> dict:
        return {c: i for i, c in enumerate(s)}

    def shouldPop(self, stk: list, c: str, i: int, last: dict) -> bool:
        return stk and stk[-1] > c and last[stk[-1]] > i