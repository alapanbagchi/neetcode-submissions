class Solution:
    def is_number(self, num: str) -> bool:
        try:
            float(num)
            return True
        except:
            return False
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        for token in tokens:
            if self.is_number(token):
                stack.append(int(token))
            else:
                second_num = stack.pop()
                first_num = stack.pop()
                if token == '+':
                    stack.append(first_num+second_num)
                elif token == '*':
                    stack.append(first_num*second_num)
                elif token == "/":
                    stack.append(int(first_num/second_num))
                else:
                    stack.append(first_num-second_num)
        
        return stack[0]