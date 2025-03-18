class Solution:
    
    def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
        """
        Algo:
        - for each spell, we have to multiply with every potion and check if the product is more than the success number
        - we can reduce it to a lookup instead by getting the least multiplier , success/spell. this way it is a lookup problem
        - if we sort the potions list then , we can easily find the number of potiopns greater than the multiplier we need
        - we implement a dictionary to avoid duplicating checks for the duplicate spells 
        """
        total_potions = len(potions)
        answer = []
        #sort potions
        potions.sort()
        spell_success_counts = {} # map of spell and its success number so we can save on repeating calculations for duplicate spells

        for spell in spells:
            
            if (spell not in spell_success_counts.keys()):
                target = success / spell
                if potions[-1] < target:
                    spell_success_counts.update({spell:0})
                    answer.append(0)
                elif potions[0] >= target:
                    spell_success_counts.update({spell:total_potions})
                    answer.append(total_potions)
                else:
                    start, end = 0, total_potions -1 
                    insertion_point = total_potions # critical because we want to find the leftmost index where target can be inserted without disturbing the sorted order
                    while (start<=end):
                        mid = (start + end) // 2 
                        if potions[mid] >= target: # we have to move left
                            insertion_point = mid
                            end = mid - 1  
                        else: # we have to move right
                            start = mid + 1
                        
                    count = total_potions- insertion_point
                    spell_success_counts.update({spell:count})
                    answer.append(count)
            else:
                answer.append(spell_success_counts[spell])
            
        print(answer)
        return answer

spells = [36,36,22,11,35,21,4,25,30,35,31,10,8,39,7,22,18,9,23,30,9,37,22,7,36,40,17,37,38,27,6,15,1,15,7,31,36,29,9,15,3,37,15,17,25,35,9,21,5,17,25,8,18,25,7,19,4,33,9,5,29,13,9,18,5,10,31,6,7,24,13,11,8,19,2]
potions = [30,11,5,20,19,36,39,24,20,37,33,22,32,28,36,24,40,27,36,37,38,23,39,11,40,19,37,32,25,29,28,37,31,36,32,40,38,22,17,38,20,33,29,17,36,33,35,25,28,18,17,19,40,27,40,28,40,40,40,39,17,34,36,11,22,29,22,35,35,22,18,34]

assert Solution.successfulPairs(spells,potions,135) == [72,72,71,68,72,71,29,71,72,72,72,68,68,72,59,71,71,68,71,72,68,72,71,59,72,72,71,72,72,72,51,71,0,71,59,72,72,72,68,71,0,72,71,71,71,72,68,71,46,71,71,68,71,71,59,71,29,72,68,46,72,71,68,71,46,68,72,51,59,71,71,68,68,71,0]