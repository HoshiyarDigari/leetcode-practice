
def kidsWithCandies(candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        answer = []
        for item in candies:
            # we now compare this item + extracandies with rest of the items in the candies list
            add_to_answer = True
            compare_list = [x for x in candies if x!=item]
            print(compare_list, 'compare', item)
            for value in compare_list:
                   if value > item + extraCandies:
                          add_to_answer = False
            if add_to_answer:
                answer.append('True')
            else:
                answer.append('False')
        print(answer, 'answer')           
            
                  
if __name__ == "__main__":
        candies = [2,3,5,1,3]
        extraCandies = 3
        kidsWithCandies(candies, extraCandies)