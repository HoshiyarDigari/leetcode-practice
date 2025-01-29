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
    seen_numbers={}
    for i in range(max(len(nums1), len(nums2))):
        if i < len(nums1):
            if nums1[i] not in seen_numbers:
                seen_numbers[nums1[i]] = 1
            else:
                if seen_numbers[nums1[i]] == 3:
                    seen_numbers[nums1[i]] =2
        if i < len(nums2):
            if nums2[i] in seen_numbers:
                    seen_numbers[nums2[i]] = 2
            else:
                    seen_numbers[nums2[i]] =3
        print(seen_numbers)
    answer = [[],[]]
    answer[0] = [x for x in seen_numbers if seen_numbers[x]==1]
    answer[1] = [x for x in seen_numbers if seen_numbers[x] == 3]
    
    print(answer)

if __name__ == "__main__":
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    findDifference(nums1, nums2)