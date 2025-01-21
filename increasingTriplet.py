def increasingTriplet(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # save the list to the right of number being examined
        right_list = []
        
        # find the actual  smallest number in the nums list and the list of numbers to its right
        for index  in range(len(nums)):
            # we will store the triplet sequence in the below list
            triplet = []
            #set smallest number to 1st number in the nums list
            smallest = nums[0] 
            smallest_index = 0
            print('loop  ',index, 'of ', len(nums), 'triplet array is ', triplet, 'and numbers list is ', nums)
            for i in range(len(nums)):
                if nums[i]<= smallest:
                    smallest = nums[i]
                    smallest_index = i
                    if i != len(nums)-1:
                         right_list = nums[i:]
                    else:
                         right_list =[]
            triplet.append(smallest)
            print('the smallest is ', smallest, "index ", smallest_index, 'has ', right_list , 'to its right and triplet is ', triplet)
            for i in range(1,len(right_list)):
                # use smallest to store the value of next bigger element in the right_list,if any
                print('scanning the right list ', right_list)
                if right_list[i] > smallest:
                    temp = right_list[i]
                    triplet.append(temp)
                    print('found ', temp, 'and added to triplets which is now ', triplet)
                    #update the smallest in right list
                    smallest = temp
                    if len(triplet) == 3:
                        print('triplet found', triplet)
                        return True
            # if we didn't exit, we move on to examining rest of list with the smallest number removed
            nums.pop(smallest_index)
        print('no triplet found', triplet)
        return False


# def findSmall(list):
#      for index  in range(len(nums)):
#         #set smallest number to 1st number in the nums list
#         smallest = nums[0] 
#         smallest_index = 0
#         print('loop  ',index, 'of ', len(nums), 'triplet array is ', triplet, 'and numbers list is ', nums)
#         for i in range(len(nums)):
#             if nums[i]<= smallest:
#                 smallest = nums[i]
#                 smallest_index = i
#                 if i != len(nums)-1:
#                         right_list = nums[i:]
#                 else:
#                         right_list =[]
            
        
            
            
            


#         # find the smallest value and its index
#         smallest_number = nums[0]
#         smallest_number_index = 0
#         currentList = nums
        
#         for index in range(len(nums)):
#             triplet=[]
#             print('loop', index, 'with currentList', currentList)
#             smallest_number, smallest_number_index,compareList = smallFinder(currentList, smallest_number_index)
#             print('the smallest number in this list is ', smallest_number, 'and the list to its right is ', compareList)
#             if len(compareList)<2:
                
#                 currentList.pop(smallest_number_index)
#                 print('currentList popped', currentList)
#             else:
#                  triplet.append(smallest_number)
#                  print('first else, found a list with 2 or more numbers on the right', triplet, compareList ) 
#                  for i in range(len(compareList)):
#                       smallest_number,smallest_number_index, compareList = smallFinder(compareList, smallest_number_index)
#                       print('smallest number is',smallest_number, 'at index', smallest_number_index,'in the compare list and updated compare list is ', compareList, 'triptlet is ', triplet, 'loop number is ', i)
#                       if len(compareList)<1:
#                            break
#                       else:
#                         triplet.append(smallest_number)
#                         print('second else, found a list with 1 or more numbers on the right', triplet, compareList ) 
#                         for i in range(len(compareList)):
#                             smallest_number,smallest_number_index, compareList = smallFinder(compareList, smallest_number_index)
#                             print('smallest number is',smallest_number, 'at index', smallest_number_index,'in the compare list and updated compare list is ', compareList, 'triptlet is ', triplet, 'loop number is ', i)
                        
#             if len(triplet) >=3:
#                  print("there is a triplet")
#                  return True
                    
                    
# def smallFinder(list,smallest_number_index):
#     smallest_number = list[0]
#     smallest_number_index = 0
#     if len(list) == 1:
#          return smallest_number, smallest_number_index, []
#     for index, num in enumerate(list):
            
#             if list[index]<smallest_number:
#                  smallest_number=nums[index]
#                  smallest_number_index = index
#                 #  smallest_number_index = index
#     list_to_the_right_of_smallest_number = list[smallest_number_index+1:] 
#     return smallest_number,smallest_number_index,list_to_the_right_of_smallest_number
     


if __name__ == "__main__":
    nums = [1,5,0,4,1,3]
    increasingTriplet(nums)