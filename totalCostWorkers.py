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
        #workers_interviewed = set()
        workers_hired = 0
        total_workers = len(costs)
        total_cost = 0
        frontHeap , backHeap = [],[]
        front_worker = 0
        back_worker = total_workers-1
        def add_workers(heap_type):
            nonlocal front_worker, back_worker
            if heap_type == 'front':
                
                while len(frontHeap)<candidates and front_worker <= back_worker:
                    print('checking index', front_worker , 'the front heap is ', frontHeap)
                    heapq.heappush(frontHeap, costs[front_worker])
                    front_worker+=1
                print('front worker pointer is at ', front_worker)
            elif heap_type == 'back':
                while len(backHeap)< candidates and back_worker>=front_worker:
                    print('checking index', back_worker , 'the back heap is ', backHeap)

                    heapq.heappush(backHeap, costs[back_worker])        
                    back_worker-=1
                    print('back worker pointer is at ', back_worker)

           
        add_workers('front')
        add_workers('back')   
        print('################# INITIALIZED\n',frontHeap, backHeap)
        

        # hiring sessions
        for _ in range(k):
            #peek and compare the values in the two heaps
            while frontHeap and backHeap and workers_hired<k:
                if frontHeap[0] <=backHeap[0]:
                    total_cost+=frontHeap[0]
                    heapq.heappop(frontHeap)
                    workers_hired+=1
                    #add next available worker to the heap
                    add_workers('front')
                    print('total cost updated from front heap element', total_cost,'heap updated to', frontHeap)
                else:
                    total_cost+=backHeap[0]
                    heapq.heappop(backHeap)
                    workers_hired+=1
                    add_workers('back')
                    print('total cost updated from back heap element', total_cost,'heap updated to', backHeap)
            else:
                if workers_hired == k:
                    print('returning as all required workers hired during while')
                    return total_cost
                else:
                    while(workers_hired<k):
                        if frontHeap:
                            total_cost+=heapq.heappop(frontHeap)
                            workers_hired+=1
                        elif backHeap:
                            total_cost+=heapq.heappop(backHeap)
                            workers_hired+=1
                    print('total cost now after else', total_cost)
                    return total_cost


assert Solution.totalCostWorkers([17,12,10,2,7,2,11,20,8],3,4) == 11
assert Solution.totalCostWorkers([1,2,4,1],3,3) == 4
assert Solution.totalCostWorkers([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],11,2)==423
