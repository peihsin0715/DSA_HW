#this one didn't pass case #24/81 but didn't say why it failed

def partitionK(capacity, items, k):
    if capacity % k != 0:
        return 0
    else:
        capacity //= k
    for bag in range(k - 1):
        n = len(items)
        T = [[0] * (capacity + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(1, capacity + 1):
                T[i][w] = T[i - 1][w]
                if w >= items[i - 1]:
                    weight = T[i - 1][w - items[i - 1]] + items[i - 1]
                    if weight > T[i][w]:
                        T[i][w] = weight
        
        if T[n][capacity] != capacity:
            return 0
        else:
            i = n
            w = capacity
            used_items = []
            while i > 0 and w > 0:
                if T[i][w] == T[i - 1][w]:
                    i -= 1
                else:
                    used_items.append(i - 1)
                    w -= items[i - 1]
                    i -= 1
            for index in used_items:
                items.pop(index)
    return 1

if __name__ == '__main__':
    n = int(input())
    ipt = input()
    nums = list(map(int, ipt.split()))
    total = sum(nums)
    print(partitionK(total, nums, 3))
