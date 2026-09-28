class Solution1:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                # Track the deepest nesting level seen so far
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # Closing parenthesis reduces nesting by one level
                current_depth -= 1
        
        # The answer is simply the peak depth reached during the scan
        return max_depth


# optimized solution

class Solution2:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        current_depth = 0
        
        for char in s:
            if char == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
        
        return max_depth