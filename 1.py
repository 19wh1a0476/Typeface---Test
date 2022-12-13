import sys
from collections import deque
 
x8 = [-1, -1, 0, 1, 1, 1, 0, -1]
y8 = [0, -1, -1, -1, 0, 1, 1, 1]
 
def bfs(m, si, sj):
	q = deque()
	q.append((si, sj))
	m[si][sj] = 0
	while(len(q) > 0):
		pidx = q.popleft()
		for i in range(8):
			ci = pidx[0] + x8[i]
			cj = pidx[1] + y8[i]
			if (ci >= 0 and ci < len(m) and cj >= 0 and cj < len(m[0]) and m[ci][cj] != 0):
				m[ci][cj] = 0
				q.append((ci, cj))
		
 
def countIsolatedWhitePatches(m):
	count = 0
	ans=[]
	for i in range(len(m)):
		for j in range(len(m[0])):
			if (m[i][j] == 1):
				bfs(m, i, j)
				count += 1 # this variable gives the number of white patches
				ans.append([i,j])  # ans contains the CenterX and Center Y of the white patch
	return ans
 
