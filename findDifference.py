def findDifference(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[List[int]]
    algo:
    - walk through the lists simultaneously 
    - we will note the seen numbers in a dictionary
        if number from list1 is not in dictionary
            - add to dictionary with value 1
        if number from list2 is in dictionary
            -  and its value is 1, change value to 2
        if number form list2 is not in dictionary
            - add to list with value 3
    - all keys with value 1 are first list of answer
    - all keys with value 3 are second list of answer
    """
    seen_numbers={1:set(), 2:set(), 3:set()}
    all_seen = set()
    
    for i in range(max(len(nums1), len(nums2))):
        if i < len(nums1):
            
            if nums1[i] not in all_seen:
                seen_numbers[1].add(nums1[i]) 
                print('added', nums1[i], 'to key 1 in dictionary')
            else:
                if nums1[i] in seen_numbers[3]:
                    seen_numbers[3].remove(nums1[i])
                    seen_numbers[2].add(nums1[i])
                    print(nums1[i], 'is in list for key 3 so removed it from there and moved to key 2 as common number', seen_numbers)
            all_seen.add(nums1[i])
        if i < len(nums2):
            if nums2[i] in seen_numbers[1]:
                    seen_numbers[2].add(nums2[i]) 
                    seen_numbers[1].remove(nums2[i])
            elif nums2[i] not in seen_numbers[2]:
                    seen_numbers[3].add(nums2[i]) 
                    print('added', nums2[i], 'to key 3 in dictionary')
            all_seen.add(nums2[i])
        print(seen_numbers)
    answer = [list(seen_numbers[1]), list(seen_numbers[3])]
    # answer[0] = [x for x in seen_numbers[1]]
    # answer[1] = [x for x in seen_numbers[3]]
    
    print(answer)

if __name__ == "__main__":
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    findDifference(nums1, nums2)