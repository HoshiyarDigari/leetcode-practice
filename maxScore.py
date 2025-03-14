from collections import deque
import heapq
class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        Algo:
        - its not feasible to test all possible combinations of the indices 
        - nums2 is the limiting factor for getting the maxScore
        - we use a minHeap to keep track of the largest items from nums1 corresponding to each nums2 value.
        - this way we avoid checking combinations where nums2 value is minimum but the sum of nums1 indices of that group is lower.
        """
        #create tuples (nums2, nums1, index)
        records = []
        for i in range(len(nums2)):
            records.append((nums2[i], nums1[i], i))
        # sort these records as per nums2 value, sort sorts the list in place by each item, lambda makes the first value as key for sorting
        records.sort(key=lambda x:x[0], reverse=True)
        

        
        pq = []
        
        current_sum = 0
        current_score = 0
        maxScore = 0
        
        for n2, n1, index in records:
            
            #push the nums1 into the heap
            heapq.heappush(pq, n1)
            #update current sum
            current_sum+=n1
            
            # check if our heap exceeded the k -limit
            if len(pq) > k:
                #remove the lowest nums1 from the heap
                temp = heapq.heappop(pq)
                #reduce current sum by this nums1
                current_sum-=temp
            # if we have k items in heap , we calculate the score and update maxScore
            if len(pq)==k:
                current_score = current_sum * n2
                if current_score > maxScore:
                    maxScore = current_score
        return maxScore                

if __name__ == "__main__":
    # test case
    nums1 = [93,463,179,2488,619,2006,1561,137,53,1765,2304,1459,1768,450,1938,2054,466,331,670,1830,1550,1534,2164,1280,2277,2312,1509,867,2223,1482,2379,1032,359,1746,966,232,67,1203,2474,944,1740,1775,1799,1156,1982,1416,511,1167,1334,2344]
    nums2 = [345,229,976,2086,567,726,1640,2451,1829,77,1631,306,2032,2497,551,2005,2009,1855,1685,729,2498,2204,588,474,693,30,2051,1126,1293,1378,1693,1995,2188,1284,1414,1618,2005,1005,1890,30,895,155,526,682,2454,278,999,1417,1682,995]
    k= 42
    answer = Solution()
    #assert answer.maxScore(nums1,nums2, k)== 26653494
    
    #test1
    nums1 = [2,1,14,12]
    nums2 = [11,7,13,6]
    k = 2
    answer = Solution()
    #assert answer.maxScore(nums1, nums2, k) == 176

    #test1
    nums1 = [23,16,20,7,3]
    nums2 = [19,21,22,22,12]
    k = 3
    answer = Solution()
    assert answer.maxScore(nums1, nums2, k) == 1121

    #test2
    nums2 = [22,30,25,25,9,18]
    nums1 = [22,5,25,15,28,1]
    k = 3
    answer = Solution()
    assert answer.maxScore(nums1,nums2,k) == 1364