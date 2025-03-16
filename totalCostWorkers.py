from collections import deque
import heapq
class Solution:
    def totalCostWorkers(costs: list[int], k: int, candidates: int) -> int:
        """
        Algo:
        1. create two minheaps front and back that contain candidates workers
        2. Each round peek at the heaps and take the smaller one, if tie front one is selected
        3. remove the selected element from the original list
        4. if there are more unheaped items, add to the heap from which worker was selected
        """
        #create heaps
        workers_interviewed = set()
        workers_hired = 0
        total_workers = len(costs)
        total_cost = 0
        frontHeap , backHeap = [],[]
        def add_workers(heap_type):
            print('adding workers to', workers_interviewed)
            if heap_type == 'front':
                print('adding to front heap', frontHeap)
                i=0
                while len(frontHeap)<candidates and len(workers_interviewed)!=total_workers:
                    print('checking index', i , 'lenght of front heap is' , len(frontHeap), 'and candidates are', candidates)
                    if i not in workers_interviewed:
                        print(i, 'not in workers interviewed', workers_interviewed)
                        heapq.heappush(frontHeap, costs[i])
                        print('front heap updated to ', frontHeap)
                        workers_interviewed.add(i)
                    i+=1
            elif heap_type == 'back':
                i=total_workers-1
                while len(backHeap)<=k and len(workers_interviewed)<=total_workers and i>0:
                    print('checking index', i)
                    if i not in workers_interviewed:
                        print(i, 'not in workers interviewed', workers_interviewed)
                        heapq.heappush(backHeap, costs[i])
                        print('back heap updated to ', backHeap)
                        workers_interviewed.add(i)
                    i-=1
            print('workers now', workers_interviewed, frontHeap, backHeap)
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

