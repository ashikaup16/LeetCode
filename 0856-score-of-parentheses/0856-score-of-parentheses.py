class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]  # The base stack starts with 0 for the outer level
        
        for char in s:
            if char == '(':
                stack.append(0)
            else:
                # Pop the inner score until we hit the corresponding '0' (representing '(')
                inner_score = stack.pop()
                
                # If inner_score is 0, it means we closed a "()" pair (score = 1)
                # Otherwise, it's a nested pair "(A)" where score = 2 * inner_score
                add_score = 1 if inner_score == 0 else 2 * inner_score
                
                # Add this score to the previous block on top of the stack
                stack[-1] += add_score
                
        return stack[0]