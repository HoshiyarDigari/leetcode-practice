def longestOnes(nums, k):
     """
     :type nums: List[int]
     :type k: int
     :rtype: int

     algo:
     we can flip atmost k 0's, so we can have a window that has at most k 0's and rest of them are 1's. This is our initial window as we scan from left to right.
     then we move to next window and add or subtract 1 as needed account for incoming on right and outgoing on left. If our k constraint is good, we increase this window size.
     if exceeded, we slide the window frame to the right again keeping track of biggest window we have seen so far.
     """
     zero_count = 0
     left = 0
     right = 0
     max_ones =0
     #get first window of maximum ones
     print(nums)
     for right in range(len(nums)):
          print('looking at ', nums[left:right+1])
          if nums[right] == 0:
               zero_count+=1
          # right is increased by the for loop , so we don't write an else statement
          while zero_count > k:
               if nums[left] == 0:
                    zero_count-=1
               left+=1
          print('(', left, ',', right, ') count of zero is ', zero_count)
          max_ones = max(max_ones, right -left +1)
          print(max_ones)
     print(max_ones)
     return max_ones     


          
          
              
        
              
              






if __name__ == "__main__":
    nums = [0]
    k = 0
    longestOnes(nums, k)