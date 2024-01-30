'''
Time complexity O(R*C)
Space complexity O(R*C)
'''

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R = len(mat)
        C = len(mat[0])
        INF = 10**20

        q = collections.deque()

        dist = [[INF] * C for _ in range(R)]

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for i in range(R):
            for j in range(C):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))

        while len(q) > 0:
            x , y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if nx >= 0 and nx < R and ny >= 0 and ny < C and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        return dist
