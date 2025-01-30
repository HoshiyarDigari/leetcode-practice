def findDifference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    algo:
    - create two sets of unique numbers corresponding to the lists
    - compare these two sets to get the difference list
    """
    unique1 = set()
    unique2 = set()
    l1 = len(nums1)
    l2 = len(nums2)

    # copy unique numbers of nums1 to unique1
    for i in range(l1):
        unique1.add(nums1[i])
    #print('nums1',nums1, 'unique1', unique1)
    # copy unique numbers of nums2 to unique2
    for i in range(l2):
        unique2.add(nums2[i])
    #print('nums1',nums2, 'unique2', unique2)
    
    answer = [[],[]]
    # build answer list for nums1 
    for number in unique1:
        if number not in unique2:
            answer[0].append(number)
    #build answer list for nums2
    for number in unique2:
        if number not in unique1:
            answer[1].append(number)
    
    #print(answer)
    return answer


if __name__ == "__main__":
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    findDifference(nums1, nums2)