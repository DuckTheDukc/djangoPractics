from collections import deque

class Graph:
    def __init__(self, edges: list[tuple[int]], n: int) -> None:
        self.adj_list = [None] * n
        self.visited = [False] * n

        for i in range(n):
            self.adj_list[i] = []
 
        for (src, dest, weight) in edges:
            self.adj_list[src].append((dest, weight))

    def add_edge(self, edge: tuple[int]):
      self.adj_list[edge[0]].append((edge[1], edge[2]))
            
    def print(self):
      for src in range(len(self.adj_list)):
        for (dest, weight) in self.adj_list[src]:
          print(f'[{src} -> {dest} Вес: {weight}]', end=' ')
        print()

    def dfs(self):
        for i in range(len(self.adj_list)):
            if not self.visited[i]:
              for (dest, weight) in self.adj_list[i]:
                print(f'[{i} -> {dest} Вес: {weight}]', end=' ')
              self.visited[i] = True
              self.dfs()
  
    def bfs(self):
      visited = set()
      queue = deque([0])

      while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            
            for i in range(len(self.adj_list)):
              for j in self.adj_list[i]:
                if i not in visited:
                    queue.append(i)
                    
      for i in range(len(self.adj_list)):
        for (dest, weight) in self.adj_list[i]:
              print(f'[{i} -> {dest} Вес: {weight}]', end=' ')