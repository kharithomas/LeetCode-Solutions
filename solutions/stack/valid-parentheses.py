# TC : O(n)
# SC : O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in brackets.values():
                stack.append(c)
            else:
                if len(stack) == 0 or stack.pop() != brackets[c]:
                    return False

        return len(stack) == 0


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid(")(){}"))
print(s.isValid("(("))
print(s.isValid("]"))
