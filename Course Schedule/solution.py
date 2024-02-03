'''
Time complexity O(E + V)
Space complexity O(E + V)
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preq_list = collections.defaultdict(list)

        BLACK = 0
        GRAY = 1
        WHITE = 2
        taken = [BLACK] * numCourses
        print(taken)

        for a, b in prerequisites:
            preq_list[a].append(b)

        def take(x):
            taken[x] = GRAY

            for prereq in preq_list[x] :
                if taken[prereq] == GRAY:
                    return False
                if taken[prereq] == BLACK:
                    if not take(prereq):
                        return False

            taken[x] = WHITE

            return True
        
        for i in range(numCourses):
            if taken[i] == BLACK:
                if not take(i):
                    return False
        
        return True