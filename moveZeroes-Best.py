def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # all the 0's need to be at the end, so at the beginning, we need to make sure we have non-zero element at the beginning.
        non_zero_index = 0
        # walk through the list till we find a non zero element and we need to bring it to the beginning
        for index in range(len(nums)):
            
            if nums[index]!=0:
                # swap this non zero element with the one at non zero index
                nums[non_zero_index], nums[index] = nums[index], nums[non_zero_index]
                # move one step ahead and make sure this place is non zero too
                non_zero_index+=1
        return nums

if __name__ == "__main__":
    s = [0]
    moveZeroes(s)