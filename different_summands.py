def optimal_summands(n):
    summands = []
    # write your code here
    i = 1
    while n > 0:
        if n <= 2 * i:
            summands.append(n)
            n -= n
        else:
            summands.append(i)
            n -= i
            i += 1
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
