import time, math
class Solution:
    
        def minEatingSpeed(piles: list[int], h: int) -> int:
            """
            Algo:
            1. sort the piles 
            2. Koko can eat from 1 to the max number in the pile per hour
            3. if we have same number of piles as number of hours, she has to eat the maximum number to finish all piles
            4. if not, we have to find the minimum number that will allow her to eat all of them in the h hours. 
            5. we do a binary search in the search space of 1 to max to find this number.
            """
            eating_speed = float('inf') # we will respond with lowest possible rate of eating
            total_piles = len(piles)
            #sort piles
            piles.sort()
            # quick exit 
            if h == total_piles:
                return piles[-1] #she has to eat the biggest pile in one go to finish in time
            #binary search
            start = 1
            end = piles[-1]
            while (start<=end or eating_speed == 'inf'):
                mid = (start+end)//2
                time_to_finish = 0
                for bananas in piles:
                    time_to_finish= time_to_finish + math.ceil(bananas/mid)
                    if time_to_finish>h:
                        break
                    
                if time_to_finish <= h:
                    eating_speed = min(eating_speed, mid)
                    #check if we can get a slower eating rate
                    end = mid - 1
                else: # ate too slow
                     start = mid + 1 
                
            print(eating_speed)
            return eating_speed
            


            


if __name__ == '__main__':
    #test1
    start_time = time.perf_counter()
    piles = [4]
    h = 3
    assert Solution.minEatingSpeed(piles, h) in {2 }
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )

    #test2
    start_time = time.perf_counter()
    piles = [30,11,23,4,20]
    h =5
    assert Solution.minEatingSpeed(piles,h) in {30 }
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )