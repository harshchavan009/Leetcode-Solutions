from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Courses with no prerequisites
        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        order = []

        # Topological sort
        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If not all courses were processed, there is a cycle
        if len(order) != numCourses:
            return []

        return order