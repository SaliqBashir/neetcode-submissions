class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = [0] * len(position)
        for i in range(len(position)):
            pos_time[i] = (position[i], (target - position[i]) / speed[i])
        pos_time.sort(reverse=True)
        car_fleet = []
        for pos, time in pos_time:
            if not car_fleet or time > car_fleet[-1]:
                car_fleet.append(time)
        return len(car_fleet)