class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivingAsteroids = list()
        positiveAsteroidStack = list()
        
        for nextAsteroid in asteroids:
            if nextAsteroid > 0:
                positiveAsteroidStack.append(nextAsteroid)
                
            else:
                while positiveAsteroidStack:
                    positiveAsteroid = positiveAsteroidStack.pop()
                    
                    if positiveAsteroid > abs(nextAsteroid):
                        nextAsteroid = 0
                        positiveAsteroidStack.append(positiveAsteroid)
                        break
                        
                    elif positiveAsteroid == abs(nextAsteroid):
                        nextAsteroid = 0
                        break
                        
                if not positiveAsteroidStack and nextAsteroid:
                    survivingAsteroids.append(nextAsteroid)
        
        survivingAsteroids.extend(positiveAsteroidStack)
        return survivingAsteroids
