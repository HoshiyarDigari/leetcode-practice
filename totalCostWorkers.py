from collections import deque
import heapq
class Solution:
    def totalCostWorkers(costs: list[int], k: int, candidates: int) -> int:
        """
        Algo:
        1. create two minheaps front and back that contain candidates workers
        2. use two pointer front worker and backWorker to track indexes that have been interviewed
        3. Each round peek at the heaps and take the smaller one, if tie front one is selected
        4. if there are more unheaped items, add to the heap from which worker was selected
        """
        #create heaps
       
        workers_hired = 0
        total_workers = len(costs)
        total_cost = 0
        frontHeap , backHeap = [],[]
        front_worker, back_worker = 0, total_workers-1

        while workers_hired < k:
            #initialize heaps      
            while len(frontHeap)<candidates and front_worker <= back_worker:
                heapq.heappush(frontHeap, costs[front_worker])
                front_worker+=1
            while len(backHeap)< candidates and back_worker>=front_worker:
                heapq.heappush(backHeap, costs[back_worker])        
                back_worker-=1

            #hiring sessions
            if frontHeap and backHeap:         
                if frontHeap[0] <=backHeap[0]:
                    total_cost+=heapq.heappop(frontHeap)
                else:
                    total_cost+=heapq.heappop(backHeap)
            else:
                if frontHeap:
                    total_cost+=heapq.heappop(frontHeap)
                else:
                    total_cost+=heapq.heappop(backHeap)
            workers_hired+=1
        
        return total_cost
                    

assert Solution.totalCostWorkers([17,12,10,2,7,2,11,20,8],3,4) == 11
assert Solution.totalCostWorkers([1,2,4,1],3,3) == 4
assert Solution.totalCostWorkers([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],11,2)==423
