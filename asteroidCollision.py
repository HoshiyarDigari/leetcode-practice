
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
    print('list of asteroids', asteroids)
    i=0
  
    while i < len(asteroids):
        oppositeSigns = False
        print('next steroid at index ',i, 'with value', asteroids[i], 'current stack', stack)
        
        # if the product of two numbers is less than 0 , they are of opposite signs 
        if len(stack)>0:
            print('opposite sign being  evaluated to', oppositeSigns)
            oppositeSigns = ((asteroids[i]* stack[-1]) < 0)
            
        if oppositeSigns and stack[-1]>0:
            print('opposite signs detected, current stack is ', stack)
            if abs(stack[-1]) == abs(asteroids[i]):
                stack.pop()
                print('popped stack', stack)
            elif abs(stack[-1]) < abs(asteroids[i]):
                # in this case, we have to replace the top of stack, but we have to also check that after popping, the element on current top is same sign or not. it will collide again if of opposite sign
                stack.pop()
                #check if stack is empty
                if not stack:
                    stack.append(asteroids[i])
                else:
                    print('stack popped because incoming asteroid is colliding and bigger', asteroids[i], stack)
                    continue
            
        else:
            stack.append(asteroids[i])
        i+=1
    print(stack)
    

if __name__ == "__main__":
    asteroids = [-2,-1,1,2]
    asteroidCollision(asteroids)