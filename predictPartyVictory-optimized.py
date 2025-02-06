from collections import deque
def predictPartyVictory(senate: str) -> str:
    """
    Track each senator’s position using deques (R_indexes and D_indexes).
    Compare the front elements of both queues.
    The senator with the smaller index bans the other.
    The winner moves to the next round by adding index + length to the queue.
    Repeat until one queue is empty.
    """
    length = len(senate)
    R_indexes = deque(x for x in range(length) if senate[x]== 'R' )
    D_indexes = deque(x for x in range(length) if senate[x] == 'D')
    while D_indexes and R_indexes:
        
        print(D_indexes, R_indexes)
        if D_indexes[0] < R_indexes[0]:
            R_indexes.popleft()
            D_indexes.append(D_indexes.popleft()+ length)
        else:
            D_indexes.popleft()
            R_indexes.append(R_indexes.popleft()+ length)
    print( 'Dire' if D_indexes else 'Radiant')
            
    

    
    



if __name__ == "__main__":
    senate = "RDRDDDR"
    predictPartyVictory(senate)