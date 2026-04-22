class Solution:
    def isValid(self, s: str) -> bool:

        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        stack = []

        # "([{}])"

        for c in s:
            # if closed
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False

            # if open
            else:
                stack.append(c)

        return True if not stack else False


            


