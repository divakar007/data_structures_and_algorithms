class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        if len(prerequisites) == 0:
            return [x for x in range(numCourses)]
        for u,v  in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        stack = []
        for course in range(numCourses):
            if indegree[course] == 0:
                stack.append(course)
            
        result = []

        visited = set()
        while stack:
            course = stack.pop(-1)
            
            if course not in visited:
                result.append(course)
                visited.add(course)
                for nei in graph[course]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        stack.append(nei)
        
        return result if len(visited) == numCourses else []