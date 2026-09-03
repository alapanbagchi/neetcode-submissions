class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # -c1(3)--c2(2)-----x
        # Time for c2 = 3hr
        # Time for c1 = 3hr

        # c3(1)c2(2)--c1(2)--c4(1)--x
        # Time for c4 = 3hr
        # Time for c1 = 3hr
        # Time for c2 = 4.5hr
        # Time for c3 = 9

        pos_speed_pair = [(pos,speed) for pos, speed in zip(position,speed)]
        pos_speed_pair.sort(reverse=True)
        total_car_fleets = 0
        stack = [(target - pos_speed_pair[0][0])/pos_speed_pair[0][1]]
        for pos, speed in pos_speed_pair:
            time = (target-pos)/speed
            if stack and time > stack[-1]:
                stack.append(time)
        return len(stack)
            
            