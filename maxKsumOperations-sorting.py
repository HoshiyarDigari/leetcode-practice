def maxOperations(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        algo:
        sort the input array
        if current left and right are a pair: increase complement count and move pointers inwards
        else if their sum is greater than K, move right inwards because we need a smaller number to add upto k
        else move left inwards
        """
        # we scan from both ends checking if list has their complements to sum up to k, if yes remove them from list , until left crosses right
        left = 0
        right = len(nums)-1
        operations = 0 

        array = sorted(nums)
        print(array)
        while left < right:
            if array[left] + array[right] == k:
                    operations+=1
                    left+=1
                    right-=1
            elif array[left] + array[right] > k:
                  right-=1
            else:
                  left+=1
        print(operations)
        return operations
if __name__ == "__main__":
    nums=[1,2,3,4]
    k = 5
    maxOperations(nums, k)