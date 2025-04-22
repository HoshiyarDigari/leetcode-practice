import time
class Solution:
    
    def findPeakElement( nums: list[int]) -> int:
        """
        Algo:
        1. this is very straightforward application of binary search for a peak
        2. check the mid is a peak or not and keep going leftwards, if not found go right
        3. edge cases:
            -single item - return the same
            - two items - return the greater one but if they are equal, this might not be good, just go through the binary search then
        """

        #single item
        if len(nums)==1:
            return 0
        #check for first and last elements are peak or not
        total_nums= len(nums)
        if nums[0]>nums[1]:
            return 0
        if nums[-1]>nums[-2]:
            return total_nums-1
        #binary search
        start = 0
        end = total_nums - 1
        #search left half
        while start <= end:
            mid = (start + end)//2
            #check if left of mid is within the list
            left_neighbor = float('-inf') if mid-1 < 0 else nums[mid -1]
            right_neighbor = nums[mid + 1] # since we are moving in left half, the right neighbor will always be within the list
            if nums[mid] > left_neighbor and nums[mid]> right_neighbor:
                return mid
            elif left_neighbor > nums[mid]: # move left 
                end = mid - 1
            else:
                start = mid + 1
        return None

            


if __name__ == '__main__':
    #test1
    start_time = time.perf_counter()
    nums = [3,4,3,2,1]
    assert Solution.findPeakElement(nums) in {1, 5 }
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )

    #test2
    start_time = time.perf_counter()
    nums = [1,2,3,1]
    assert Solution.findPeakElement(nums) in {2 }
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )