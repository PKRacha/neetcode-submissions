"""
# BruteForce: Remove all the characters except brackets. 
#               Then replace {}, [], () until such a combination exists. 
                If the string is empty return true.
            TC: O(n2) and SC: O(n)
    Stack approach:
        - Create a dictionary of closing bracket as the key and opening bracket type as value. 
            This will help us extend to other combinations easily
            Also, loop time is quick
        Iterate through the string:
            - For non braces simply move forward to next character
            - If we find any opening braces type, push to stack
            - If we find any closing braces type, pop and compare to stack
                - If the character does not match, then return false
            - At the end return True if stack is empty, otherwise false
        TC: O(n) and SC: O(n)

"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False