import heapq
class Solution:
    def findKthLargest(nums: list[int], k: int) -> int:
        """
        Algo:
        Use a maxm Heap to find the kth element in the heap. howevever heapq.heapify does minHeap.
        So, we negate the values before heapifying it
        """
        negative_nums = [-x for x in nums]
        heapq.heapify(negative_nums)
        #we pop elements till we hit the kth element
        for i in range(k-1):
            heapq.heappop(negative_nums)
        print(negative_nums)
        #return the element at the top now but negate it again to get original value
        return -negative_nums[0]

if __name__ == "__main__":
    #test case 1
    nums = [3,2,1,5,6,4]
    k = 3
    assert Solution.findKthLargest(nums,k) == 4
