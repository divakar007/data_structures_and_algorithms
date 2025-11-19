class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        
        cars = [(pos, s) for pos, s in zip(position, speed)]
        cars.sort()

        carFleets = 0
        time = 0
        while cars:
            pos, s = cars[-1]
            requiredTime = float(target - pos)/s
            if time < requiredTime:
                time = requiredTime
                carFleets += 1
            
            cars.pop()
        
        return carFleets