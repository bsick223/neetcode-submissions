class Solution:
    def isValid(self, s: str) -> bool:


    # input is a string

    # output is boolean, and true if the paranethesis are opened and closed properly..

        stack = []

        closeToOpen = {")": "(", "]" : "[", "}" : "{"}

        for c in s:

            if c not in closeToOpen:
                stack.append(c)

            else:
                if not stack:
                    return False
                else:
                    if closeToOpen[c] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        
        return True if not stack else False
                