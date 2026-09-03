class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 30, 38, 30, 36, 35, 40, 28
        # Output: []
        # Stack: [(30,0), (38,1)]
        # Output: [1,]
        # Stack: [(38,1), (30,2), (36, 3)]
        # Output: [1, _, 1]
        # Stack: [(38,1), (36,3)]
        # Stack: [(38,1), (36,3), (35, 4), (40,5)]
        # Output: [1,4,1,2,1,0,0]

        res = [0]*len(temperatures)
        stack=[]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                res[stack[-1][1]] = index - stack[-1][1]
                stack.pop()
            stack.append((temp, index))
        
        return res