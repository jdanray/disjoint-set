class Edge:
	def __init__(self, u, v, w):
		self.u = u
		self.v = v
		self.w = w

class DisjointSet:
	def __init__(self, N):
		self.id = range(N)
		self.rank = [1] * N

	def find(self, x):
		if self.id[x] != self.id[self.id[x]]:
			self.id[x] = self.find(self.id[x])
		return self.id[x]

	def union(self, x, y):
		xx = self.find(x)
		yy = self.find(y)
		if xx == yy:
			return False
		elif self.rank[xx] > self.rank[yy]:
			xx, yy = yy, xx
		elif self.rank[xx] == self.rank[yy]:
			self.rank[yy] += 1
		self.id[xx] = yy
		return True

def kruskal(edges, N):
	uf = DisjointSet(N)
	trees = []
	for e in sorted(edges, key=lambda x: x.w): 
		uf.union(e.u, e.v) and trees.append(e)
	return trees
