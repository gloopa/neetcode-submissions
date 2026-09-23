class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        queue = deque([(0, -1)]) 
        seen = set([0])
        result = []

        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        
        while queue:
            node, parent = queue.popleft() 
            result.append(node)
            for nei in adjlist[node]:
                if nei == parent:
                    continue 
                elif nei in seen:
                    return False
                else:
                    seen.add(nei)
                    queue.append((nei, node))

        if len(edges) == n-1 and len(result) == n:
            return True
        else:
            return False
        

        