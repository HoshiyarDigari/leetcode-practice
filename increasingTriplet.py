def increasingTriplet(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
            
        # Initialize two variables to represent the smallest and second smallest numbers
        first = float('inf')
        second = float('inf')
        print('first and second are ', first, second,nums)
        for num in nums:
            print('checking', num)
            if num <= first:
                print('first is now', num)
                first = num  # Update the smallest number
            elif num <= second:
                print('second is now', num)
                second = num  # Update the second smallest number
            else:
                # If we find a number greater than both, a triplet exists
                print('third is ', num)
                return True
        
        return False

        
#         # save the list to the right of number being examined
#         right_list = nums
#         max = 0

#         for i in range(len(nums)):
            
#             right_list = nums
#             triplet = []
#             #print('loop',i, 'of', len(nums), 'number list is ', nums, 'triplet is ', triplet, 'right list is ', right_list)
#             while right_list and max < 15:
#                 max+=1
#                 smallest, right_list, smallest_index = findSmall(right_list, triplet)
#                 if len(triplet)!=0:
#                     if smallest > triplet[-1]:
#                         triplet.append(smallest)
#                         if len(triplet)==3:
#                             print('triplet found', triplet)
#                             return True
#                 else:
#                      triplet.append(smallest)
#                      nums.pop(smallest_index)
#                 print('function call done : smallest is ', smallest, ' triplet is ', triplet)
#         print('no triplets')
#         return False  



# def findSmall(list, triplet):
#      #for index  in range(len(list)):
#         #set smallest number to 1st number in the nums list
#     smallest = list[0] 
#     smallest_index = 0
#     if len(list)== 1:
#         right_list = []
#     else:
#         right_list = list
#     for i in range(len(list)):
#         #print('loop line 41  ',i, 'of ', len(list), 'and numbers list is ', list, ' smallest is ', smallest, 'current index values is ', list[i], 'at index ', i)
#         if not triplet:  
#             if list[i]< smallest:
#                 # print('no triplet,updating smallest to ', list[i])
#                 smallest = list[i]
#                 smallest_index = i
#                 if i <= len(list)-2:
#                         right_list = list[i+1:]
#                 else:
#                         right_list =[]
#                 # print('loop  ',i, 'of ', len(list), 'and smallest number is ', smallest, 'at', smallest_index, 'and  numbers list is ', list)
#         elif triplet:
#             if list[i]< smallest:
#                 #print('updating smallest to ', list[i] , triplet)
#                 if list[i] > triplet[-1]:
#                     smallest = list[i]
#                     smallest_index = i
#             if smallest_index <= len(list)-2:
#                 right_list = list[smallest_index+1:]
#             else:
#                 right_list =[]
                
                  
    
#     return smallest, right_list, smallest_index    

if __name__ == "__main__":
    nums = [9,10,5,11,10,9,8]
    increasingTriplet(nums)