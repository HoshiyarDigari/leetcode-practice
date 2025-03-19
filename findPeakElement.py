import time
class Solution:
    
    def findPeakElement(self, nums: list[int]) -> int:
        pass


if __name__ == '__main__':

    start_time = time.perf_counter()
    nums = [1,2,1,3,5,6,4]
    assert Solution.findPeakElement(nums) in {1, 5 }
    end_time = time.perf_counter()
    exec_time = (end_time - start_time) * 1000
    print(f'function took {exec_time:.6f} miliseconds' )