class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        indegrees = [0] * numCourses
        queue = deque()
        result = []
        for course, prereq in prerequisites:
            adjlist[prereq].append(course)
            indegrees[course] +=1 
        
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            result.append(course)
            for nei in adjlist[course]:
                indegrees[nei] -=1 
                if indegrees[nei] == 0: #no dependecnies 
                    queue.append(nei)
        return len(result) == numCourses


        

        
        