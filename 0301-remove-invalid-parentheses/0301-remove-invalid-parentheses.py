class Solution(object):
    def removeInvalidParentheses(self, s):
        """:type s: str
        :rtype: List[str]
        """
        def isValid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        if not s:
            return [""]

        # BFS initialization
        queue = [s]
        visited = {s}
        res = []
        found = False

        while queue:
            level_size = len(queue)
            current_level_res = []

            for _ in range(level_size):
                curr = queue.pop(0)

                if isValid(curr):
                    current_level_res.append(curr)
                    found = True

            # If we found valid strings at this level, collect them and stop searching deeper
            if found:
                return list(set(current_level_res))

            # Generate next level states by removing one parenthesis at each index
            for curr in queue if not found else []: # (Handled via queue continuation below)
                pass

            # Standard expansion loop if not found yet
            # Re-evaluating queue processing loop for clarity:
        
        # Cleaner structure for BFS traversal:
        queue = [s]
        visited = {s}
        found = False
        res = []

        while queue:
            curr = queue.pop(0)
            
            if isValid(curr):
                res.append(curr)
                found = True
            
            if found:
                # If we found valid strings, we don't need to generate further removed states
                continue
                
            # Generate all possible states by removing one parenthesis
            for i in range(len(curr)):
                if curr[i] != '(' and curr[i] != ')':
                    continue
                next_str = curr[:i] + curr[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
                    
        return list(set(res))