from collections import deque
def predictPartyVictory(senate: str) -> str:
    queue = deque(senate)
    complement = {'R':'D', 'D':'R'}
    counter = 0
    while queue and counter < 7:
        counter +=1
        for senator in queue:
            if complement[senator] in queue:
                queue.remove(complement[senator])
                print(queue)
                break
            else:
                print('winner is ', queue[0])
                return queue[0]
    



if __name__ == "__main__":
    senate = "RDRDDDR"
    predictPartyVictory(senate)