import time
class Solution:
    def minCostClimbingStairs(cost: list[int]) -> int:
        """
        the top of the stairs is conceptual index of len(stairs), if we have 5 stairs, they are indexed 0-4, and index5 is the top. There is no cost for this step. Our function tracks the cost of stepping onto each of the stair. to get to top , we shoudl have reached either index 4 or index3, we just choose the minimum of these two. to get the cost to step onto a stair, we add its cost when we take a step onto it. 
        """
        total_stairs = len(cost)
        if total_stairs == 0:
            return 0
        if total_stairs == 1:
            return cost[0]
        if total_stairs == 2:
            return min(cost[0], cost[1])
        cost_two_step_back = cost[0]
        cost_one_step_back = cost[1]
        # now we need to do the bottoms up recurrence 
        for i in range(2, total_stairs):
            # since we decide to land on this current step, if we have to pay for it
            current_step_cost = min(cost_two_step_back,cost_one_step_back) + cost[i]
            cost_two_step_back , cost_one_step_back = cost_one_step_back, current_step_cost
        
        return min(cost_one_step_back,cost_two_step_back)
    

#test 1
#assert Solution.minCostClimbingStairs([10,15,20])==15

#assert 2

assert Solution.minCostClimbingStairs([10,15,20,30,60,70]) == 90