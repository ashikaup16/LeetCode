class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        min_adds = 0
        open_brackets = 0
        
        for char in s:
            if char == '(':
                open_brackets += 0 + 1  # Equivalent to open_brackets += 1
            else:
                if open_brackets > 0:
                    open_brackets -= 1
                else:
                    min_adds += 1
                    
        return min_adds + open_brackets