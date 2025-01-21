def increasingTriplet(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # save the list to the right of number being examined
        right_list = nums
        max = 0

        for i in range(len(nums)):
            
            right_list = nums
            triplet = []
            print('loop',i, 'of', len(nums), 'number list is ', nums, 'triplet is ', triplet, 'right list is ', right_list)
            while right_list and max < 15:
                max+=1
                smallest, right_list, smallest_index = findSmall(right_list, triplet)
                if len(triplet)!=0:
                    if smallest > triplet[-1]:
                        triplet.append(smallest)
                        if len(triplet)==3:
                            print('triplet found', triplet)
                            return True
                else:
                     triplet.append(smallest)
                     nums.pop(smallest_index)
                print('function call done : smallest is ', smallest, ' right list is ', right_list, ' triplet is ', triplet)
        print('no triplets')
        return False  



def findSmall(list, triplet):
     #for index  in range(len(list)):
        #set smallest number to 1st number in the nums list
    smallest = list[0] 
    smallest_index = 0
    right_list = list
    for i in range(len(list)):
        # print('loop line 28  ',i, 'of ', len(list), 'and numbers list is ', list, ' smallest is ', smallest, 'current index values is ', list[i])
        if not triplet:  
            if list[i]< smallest:
                # print('no triplet,updating smallest to ', list[i])
                smallest = list[i]
                smallest_index = i
                if i <= len(list)-2:
                        right_list = list[i+1:]
                else:
                        right_list =[]
                # print('loop  ',i, 'of ', len(list), 'and smallest number is ', smallest, 'at', smallest_index, 'and  numbers list is ', list)
        else:
             if list[i]< smallest and list[i] not in triplet:
                # print('updating smallest to ', list[i] , triplet[-1])
                smallest = list[i]
                smallest_index = i
                if i <= len(list)-2:
                        right_list = list[i+1:]
                else:
                        right_list =[]
             else:
                  right_list = list[1:]
    
    return smallest, right_list, smallest_index    

if __name__ == "__main__":
    nums = [9,10,5,11,10,9,8]
    increasingTriplet(nums)