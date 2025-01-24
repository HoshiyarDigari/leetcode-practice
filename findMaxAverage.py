def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        algo:
        1. use sliding window of k elements
        2. start with left= 0 , right= k-1
        3, add all items from left to right indexes and save in sum variable
        4. increase left and right by 1, till right doesn't exceed len(nums)
        5. to get the sum of next window , subtract previous left item and add the newly included right item to previous save. 
        6. check if this value is bigger than previous save, if yes add to max_sum
        """
        window_size = k
        window_start = k - window_size
        
        current_sum = 0
        # calculate sum for the first window
        for i in range(k):
              current_sum+=nums[i]
        
        # assume this is the max sum for now
        max_sum = current_sum

        # start sliding the window
        while k < len(nums) :
              print('new added element is',k, 'this window starts at', k-window_size)
              current_sum = current_sum + nums[k] - nums[k-window_size]
              if current_sum > max_sum:
                    max_sum = current_sum
              k+=1
              print(max_sum, current_sum,'sums after another round of while')
        print(max_sum/window_size)
              
                                  
if __name__ == "__main__":
    nums=[1,12,-5,-6,50,3]
    k =4
    findMaxAverage(nums, k)

