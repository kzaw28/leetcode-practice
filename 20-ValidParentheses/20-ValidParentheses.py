# Last updated: 5/27/2025, 6:45:58 PM
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # We will use a stack to store just the opening brackets and check
        # the characters in the string, whether if the latest added value in
        # stack corresponding to the current character being checked from the string

        # The result will be True or False depending on whether the stack is empty or not
        stack = []

        # A HashMap will be needed as every parenthesis needs a pair. Since we are 
        # checking the closing brackets, they are the keys.
        pairs = { ")": "(", "}": "{", "]": "[" }

        for c in s:
            if c in pairs: # If the character is a closing bracket
                # The character is not the first being added (aka stack isn't empty)
                # and the last added open bracket is corresponding to the current 
                # closing bracket being checked. 

                # This is because something like this "[(])" should be False.
                if stack and stack[-1] == pairs[c]: 
                    stack.pop()
                else:
                    return False
            else: # If the character is not a closing bracket, add it to the stack
                stack.append(c)
        
        return True if not stack else False

        
        