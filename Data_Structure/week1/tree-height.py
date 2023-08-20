import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.cache = [0] * self.n  # Cache for storing computed heights

    def compute_height(self, node):
        if self.parent[node] == -1:
            return 1
        
        if self.cache[node] != 0:
            return self.cache[node]
        
        self.cache[node] = 1 + self.compute_height(self.parent[node])
        return self.cache[node]

def main():
    tree = TreeHeight()
    tree.read()
    maxHeight = 0
    for vertex in range(tree.n):
        maxHeight = max(maxHeight, tree.compute_height(vertex))
    print(maxHeight)

threading.Thread(target=main).start()
