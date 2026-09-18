from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Graph: prerequisite -> course
        graph = [[] for _ in range(numCourses)]
        
        # indegree[i] = number of prerequisites for course i
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Courses with no prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        completed = 0

        # Topological sort
        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses