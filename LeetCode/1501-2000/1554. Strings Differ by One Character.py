class Solution:
    def differByOne(self, dict: list[str]) -> bool:
        MOD = (1 << 61) - 1
        BASE = 29

        n = len(dict)
        if n == 0:
            return False
        m = len(dict[0])

        powers = [1] * m
        for j in range(m - 2, -1, -1):
            powers[j] = (powers[j + 1] * BASE) % MOD

        seen = {}

        for s in dict:
            full_hash = 0
            for ch in s:
                full_hash = (full_hash * BASE + ord(ch)) % MOD

            for j in range(m):
                wildcard_hash = (full_hash - ord(s[j]) * powers[j]) % MOD

                if wildcard_hash in seen:
                    for stored in seen[wildcard_hash]:
                        if self.verifyMatch(stored, s, j):
                            return True

                if wildcard_hash not in seen:
                    seen[wildcard_hash] = []
                seen[wildcard_hash].append(s)

        return False

    def verifyMatch(self, s1: str, s2: str, skip_index: int) -> bool:
        for i in range(len(s1)):
            if i == skip_index:
                continue
            if s1[i] != s2[i]:
                return False
        return True