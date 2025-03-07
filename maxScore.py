class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Algo:
        we use quicksort to sort the list and then use the largest k elements from nums1 to use for sum
        """
        def quick_sort(numbers:list)->list:
            if not numbers:
                return 
            pivot = numbers[len(numbers)//2]
            greater= [x for x in numbers if x>pivot]
            lesser = [x for x in numbers if x<pivot]
            equal = [x for x in numbers if x == pivot]
            return quick_sort(greater) + equal + quick_sort(lesser)
        
        #sort nums1
        nums1_sorted = quick_sort(nums1)
        #get sum of top k elements
        maxSum=0
        for i in range(k):
            maxSum+=nums1_sorted[i]
        
        return maxSum*min(nums2)


if __name__ == "__main":

    #test1
    nums1 = [1,3,3,1]
    nums2 = [2,1,3,4]
    k = 3
    assert Solution.maxScore(nums1, nums2, k) == 12
