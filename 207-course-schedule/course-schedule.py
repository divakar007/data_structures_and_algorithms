class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        stack = []

        for course in range(numCourses):
            if indegree[course] == 0:
                stack.append(course)
        
        visited = set()
        while(stack):
            course = stack.pop(-1)

            if course not in visited:
                visited.add(course)

                for node in graph[course]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        stack.append(node)

        return len(visited) == numCourses


        