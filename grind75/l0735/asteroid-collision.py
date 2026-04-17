from typing import List


def asteroidCollision(asteroids: List[int]) -> List[int]:
    stack = []
    for asteroid in asteroids:
        if not stack or asteroid > 0:
            stack.append(asteroid)
            continue


        while stack and stack[-1] >0 and asteroid + stack[-1] < 0:
                stack.pop()
        
        if not stack or stack[-1] < 0:
            stack.append(asteroid)
        elif asteroid + stack[-1] == 0:
            stack.pop()

    return list(stack)
    
        
            