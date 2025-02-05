from collections import deque
def predictPartyVictory(senate: str) -> str:
    queue = deque(senate)
    complement = {'R':'D', 'D':'R'}
    counter = 0
    visited = set()
    removed = set()
    while queue and counter < 7:
        counter +=1
      
        for senator in queue:
            if  queue.index(senator) not in visited:
                if complement[senator] in queue and queue.index(complement[senator]) not in removed :
                    #queue.remove(complement[senator])
                    visited.add(queue.index(senator))
                    removed.add(queue.index(complement[senator]))
                    print(queue, visited,removed)
                    break
                else:
                    print('winner is ', queue[0])
                    return queue[0]
    



if __name__ == "__main__":
    senate = "RDRDDDR"
    predictPartyVictory(senate)