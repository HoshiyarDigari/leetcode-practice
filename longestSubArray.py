def longestSubarray( nums, k):
    """
    :type nums: List[int]
    :rtype: int
    algo:
    - find the longest series of 1's with k=1 , like previous longestOnes problem
    - and return one less
    """
    left = 0
    zero_count = 0
    max_length = 0 

    for right in range(len(nums)):
        if nums[right]==0:
            zero_count+=1
        while zero_count > k:
            if nums[left]==0:
                zero_count-=1
            left+=1
        max_length= max(max_length, right -left + 1)
    print(max_length, 'is max answer is 1 less')

if __name__ == "__main__":
    nums = [1,1,1]
    k = 1
    longestSubarray(nums, k)