import heapq
class Solution:
    def findKthLargest(self,nums: list[int], k: int) -> int:
        """
        Algo:
        we will use quicksort but stop when it is sorted enough to return the kth largest element. this is quick select, we dont need to do the whole sorting
        main insight is that the pivot is always in its correct place compared to left and right elements.
        we compare if this pivots place is the target place we are looking for
        """
        if not nums:
            return 
        target_index =  k-1 
        pivot = nums[len(nums)//2]
        left = [x for x in nums if x > pivot]
        right = [x for x in nums if x<pivot]
        # in case there are duplicates of selected pivot then we need to account for them 
        middle = [x for x in nums if x==pivot]
        
        #we have to account for length of the duplicates of middle to know the p_index correctly
        p_index_min = len(left)
        p_index_max = p_index_min + (len(middle)-1)
        print('left, middle,right,k',left,middle,right, k)
        if target_index in range(p_index_min, p_index_max + 1):
            print('found it , it is ', pivot)
            return pivot
        if target_index < p_index_min:
            print('recursive call for left with unchanged k')
            return self.findKthLargest(left,k)
        else: # target must be greater than p_max
            print('recursive call for right with changed k')
            return self.findKthLargest(right, target_index - p_index_max)
            

if __name__ == "__main__":
    #test case 1
    nums = [3,2,1,5,6,4]
    k = 3
    answer = Solution()
    assert answer.findKthLargest(nums,k) == 4

    #test 2
    nums = [3,2,3,1,2,4,5,5,6]
    k=4
    answer=Solution()
    assert answer.findKthLargest(nums,k) == 4

    #test 3
    nums = [-1,-1]
    k =2
    answer= Solution()
    assert answer.findKthLargest(nums,k) == -1 