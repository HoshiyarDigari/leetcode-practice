
def asteroidCollision( asteroids):
    """
    :type asteroids: List[int]
    :rtype: List[int]
    algo:
    - we scan and create a stack of the numbers in asteroid list
        - we compare if the next one into stack is opposite sign than the top element in stack
            - compare their magnitude and decide whether to put or update with max value of current top and incoming number
    - return the stack 

    """
    stack = []
    for asteroid in asteroids:
        # we only need to check if we have a right moving asteroid on top and a left moving asteroid comes along. Collisions don't happen otherwise
        print('scanner at ', asteroid, stack)
        while stack and stack[-1]>0 and asteroid < 0:
            if abs(stack[-1]) == abs(asteroid):
                stack.pop()
                break
            elif abs(stack[-1]) < abs(asteroid):
                stack.pop()
                continue
            else:
                break
           
        if not stack or asteroid>0:
            stack.append(asteroid)
            
        
    print(stack)
            

if __name__ == "__main__":
    asteroids = [5,10,-5]
    asteroidCollision(asteroids)