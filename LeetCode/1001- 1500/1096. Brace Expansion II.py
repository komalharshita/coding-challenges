class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.expr = expression
        self.pos = 0
        result = self.parseUnion()
        return sorted(result)

    def parseUnion(self) -> set[str]:
        result = self.parseConcat()
        while self.pos < len(self.expr) and self.expr[self.pos] == ',':
            self.pos += 1
            result |= self.parseConcat()
        return result

    def parseConcat(self) -> set[str]:
        result = {""}
        while self.pos < len(self.expr) and self.expr[self.pos] not in ',}':
            factor = self.parseFactor()
            result = {a + b for a in result for b in factor}
        return result

    def parseFactor(self) -> set[str]:
        if self.expr[self.pos] == '{':
            self.pos += 1
            result = self.parseUnion()
            self.pos += 1  # skip '}'
            return result
        # Single lowercase letter
        ch = self.expr[self.pos]
        self.pos += 1
        return {ch}