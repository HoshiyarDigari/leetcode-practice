def moveZeroes( nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """  
        index = 0
        counter = 0
        end = len(nums) -1 
        while index <= end and counter < 7:
            print('looking at index', index, nums[index],'end pointer is at ', end, nums[end])
            if nums[index] == 0 and index < len(nums) - 1:
                    print('replacing ', nums[index:], 'with list to its right', nums[index+1:])
                    nums[index:] = nums[index+1:]
                    nums.append(0)
                    print('appended 0 at end and nums is now', nums, 'index is at ', index)  
            elif nums[index] !=0:
                  index+=1
            if nums[end] == 0:
                  print('0 is at the end')
                  end-=1
            # counter+=1
        print(nums)
        return nums

if __name__ == "__main__":
    s = [0]
    moveZeroes(s)