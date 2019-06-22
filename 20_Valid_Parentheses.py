class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for char in s:
            if char in ('(', '[', '{'):
                stack.append(char)
            else:
                if not stack:
                    return False

                top_char = stack.pop()
                if char == ')' and top_char != '(':
                    return False
                elif char == ']' and top_char != '[':
                    return False
                elif char == '}' and top_char != '{':
                    return False

        if stack:
            return False

        return True