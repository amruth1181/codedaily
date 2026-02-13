class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # FLAG: Does the current asteroid survive the collisions?
            alive = True

            # While the current asteroid is moving LEFT (< 0)
            # AND there is a stack
            # AND the top of the stack is moving RIGHT (> 0)
            while alive and asteroid < 0 and stack and stack[-1] > 0:

                # Case 1: The positive asteroid on stack is smaller. It explodes.
                if stack[-1] < -asteroid:
                    stack.pop()
                    # The current 'asteroid' stays alive and loops to check the next one on stack.

                # Case 2: Both are equal size. Both explode.
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False  # Current one dies too

                # Case 3: The positive asteroid is bigger. Current one explodes.
                else:
                    alive = False  # Current one dies

            # If the asteroid survived all collisions (or never collided), add it
            if alive:
                stack.append(asteroid)

        return stack


