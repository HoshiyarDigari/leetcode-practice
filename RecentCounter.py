from collections import deque
class RecentCounter:
    
    def __init__(self):
        self.counter = deque()  

    def ping(self, t: int) -> int:
        # add the new time to the counter deque
        print(self.counter)
        self.counter.append(t)
        # pop times from front of deque if they are invalid
        while self.counter and self.counter[0] < t - 3000:
            self.counter.popleft()
        
        #return the size of counter
        print(self.counter,len(self.counter))
        return (len(self.counter))
    
if __name__ == "__main__":
    string = [ 1, 100, 3001, 3002, 3003, 80000] 
    r1 = RecentCounter()
    for t in string:
        r1.ping(t)