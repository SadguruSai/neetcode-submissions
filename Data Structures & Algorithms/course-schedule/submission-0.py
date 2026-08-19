class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Count prerequisites for every course.
        # 2. Put courses with 0 prerequisites into a queue.
        # 3. Take one course from the queue.
        # 4. Pretend you completed it → remove its dependency from neighbors.
        # 5. If a neighbor reaches 0 prerequisites → put it in the queue.
        # 6. Repeat.
        # 7. If you processed every course → true.
        # Otherwise → false (there is a cycle).
        graph=[[] for _ in range(numCourses)]
        preReq=[0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            preReq[a]+=1
        
        que=deque()
        for i in range(numCourses):
            if preReq[i]==0:
                que.append(i)
        completed=0

        while que:
            course=que.popleft()
            completed+=1
            for next_course in graph[course]:
                preReq[next_course]-=1
                
                if preReq[next_course]==0:
                    que.append(next_course)
        
        return completed==numCourses

