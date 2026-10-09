class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        need = 0
        
        for c in s:
            if c == '(':
                need += 2
                # If need is odd, it means we had a dangling right parenthesis 
                # previously that needs a companion. We fix it by adding ')' (ans += 1)
                # and adjusting the need count.
                if need % 2 == 1:
                    ans += 1
                    need -= 1
            else: # c == ')'
                need -= 1
                # If need < 0, we have an extra closing parenthesis with no 
                # opening bracket. We fix it by adding an opening '(' (ans += 1)
                # and resetting the requirement.
                if need < 0:
                    ans += 1
                    need += 2
                    
        # Any remaining 'need' represents missing right parentheses at the end.
        return ans + need