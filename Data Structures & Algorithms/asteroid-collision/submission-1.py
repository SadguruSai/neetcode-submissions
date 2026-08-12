class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #maintain a stack for only +ve values
        #whenever a -ve is met if same value or smaller pop if larger keep
        #return the final stack as list
        q=deque()
        for i in asteroids:
            while q and i<0 and q[-1]>0:
                if q[-1]<abs(i):
                    q.pop()
                elif q[-1]==abs(i):
                    q.pop()
                    break
                else:
                    break
            else:
                q.append(i)
        return list(q)

