def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    border = 0
    for i in range(1, m):
        while border > 0 and pattern[i] != pattern[border]:
            border = pi[border - 1]
        if pattern[i] == pattern[border]:
            border += 1
        else:
            border = 0
        pi[i] = border
    return pi

def get_occurrences(pattern, text):
    pi = compute_prefix_function(pattern)
    n = len(text)
    m = len(pattern)
    occurrences = []
    border = 0
    for i in range(n):
        while border > 0 and text[i] != pattern[border]:
            border = pi[border - 1]
        if text[i] == pattern[border]:
            border += 1
        else:
            border = 0
        if border == m:
            occurrences.append(i - m + 1)
            border = pi[border - 1]
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
