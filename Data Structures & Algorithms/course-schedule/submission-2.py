class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        indegree = [0] * numCourses
        queue = deque()
        count = 0
        for course, prereq in prerequisites:
            adjlist[prereq].append(course)
            indegree[course] += 1 
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            count+=1
            for nei in adjlist[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return count== numCourses
        


        

            
        

    




        