# TC: O(n)
# SC: O(n)

import re


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        path = re.sub("/+", "/", path)
        parts = path.split("/")

        # push path to stack
        for part in parts:
            if not part or part == '.':
                continue

            if part == '..':
                if len(stack) > 1:
                    stack.pop()
            elif part:
                stack.append(part)

        res = "/"
        # build res
        for i in range(1, len(stack)):
            res += stack[i]
            if i < len(stack) - 1:
                res += '/'

        return res


s = Solution()

print(s.simplifyPath("/home/"))
print(s.simplifyPath("/home//foo/"))
print(s.simplifyPath("/home/user/Documents/../Pictures"))
print(s.simplifyPath("/../"))
print(s.simplifyPath("/.../a/../b/c/../d/./"))
