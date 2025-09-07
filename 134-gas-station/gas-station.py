class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        total_cost = sum(cost)
        total_gas = sum(gas)

        if total_gas < total_cost:
            return -1


        start_index = 0
        curr_gas = 0
        n = len(gas)

        for i in range(n):
            curr_gas += gas[i]

            if curr_gas >= cost[i]:
                curr_gas -= cost[i]
            else:
                start_index = i+1
                curr_gas = 0
        
        return start_index
