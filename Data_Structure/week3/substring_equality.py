class Solver:
    def __init__(self, s):
        self.s = s
        self._multiplier = 263
        self._prime = 1000000007
        self.hash_values = self.compute_hash_values()

    def compute_hash_values(self):
        hash_values = [0] * (len(self.s) + 1)
        for i in range(1, len(self.s) + 1):
            hash_values[i] = (hash_values[i - 1] * self._multiplier + ord(self.s[i - 1])) % self._prime
        return hash_values

    def ask(self, a, b, l):
        hash_a = (self.hash_values[a + l] - self.hash_values[a] * pow(self._multiplier, l, self._prime)) % self._prime
        hash_b = (self.hash_values[b + l] - self.hash_values[b] * pow(self._multiplier, l, self._prime)) % self._prime
        return hash_a == hash_b

s = input()
q = int(input())
solver = Solver(s)
for i in range(q):
    a, b, l = map(int, input().split())
    print("Yes" if solver.ask(a, b, l) else "No")
