def pivotIndex( nums):
    """
    :type nums: List[int]
    :rtype: int
        algo:
        - assume first element is pivot index
        - find its left and right sums
        - move to the right of the list
           - increase left sum by previous element value
           - decrease right sum by current element value
           - do till either left sum equals right sum or we reach end of list


    """
    length = len(nums)
    left_sum = 0
    right_sum = sum(nums) - nums[0]
    if left_sum == right_sum:
        print(nums[0], 'is the pivot index')
        return 0
    else:
        
        for index in range(1,length):
            print('checking at index', index , nums[index], 'in', nums)
            left_sum+=nums[index-1]
            right_sum-=nums[index]
            print('left sum is ', left_sum , 'right sum is ', right_sum)
            if left_sum == right_sum:
                print('pivot is ', index)
                return index
        return -1



    
if __name__ == "__main__":
    nums = [1,7,3,6,5,6]
    k = 1
    pivotIndex(nums)