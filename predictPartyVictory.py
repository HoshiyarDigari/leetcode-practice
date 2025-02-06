from collections import deque
def predictPartyVictory(senate: str) -> str:
    queue = deque(senate)
    complement = {'R':'D', 'D':'R'}

    while queue:
       
        for senator in queue:
            # this senator's best plan is to remove senator from other party
            if complement[senator] in queue:
                queue.remove(complement[senator])
                #print(queue)
                # move this senator to the end of queue as his turn will now come in the next round
                queue.rotate(-1)
                #print(queue)
                break
            else:
                # if there are no complements then we only have one party's senators.
                print('winner is ', queue[0])
                return queue[0]
    



if __name__ == "__main__":
    senate = "RDRDDDR"
    predictPartyVictory(senate)