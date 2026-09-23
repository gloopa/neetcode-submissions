class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = defaultdict(list)
        result = []
        indegree = [0] * numCourses
        queue = deque()

        for course, prereq in prerequisites:
            adjlist[prereq].append(course)
            indegree[course] += 1  
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            result.append(course)
            for nei in adjlist[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(result) == numCourses:
            return result
        else:
            return []
        