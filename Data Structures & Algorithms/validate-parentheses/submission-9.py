class Solution:
    def isValid(self, s: str) -> bool:
        valid_pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']',
        }
        
        stack = []

        for c in s:
            print(stack)
            if c in valid_pairs:
                stack.append(c)
                print(c, 'is entered into the stack', stack)
            else:
                if not stack or valid_pairs[stack[-1]] != c:
                    return False
                stack.pop()
        return len(stack)==0