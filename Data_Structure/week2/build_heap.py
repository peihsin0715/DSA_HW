def sift_down(data, i, swaps):
    max_index = i
    left_child = 2 * i + 1
    if left_child < len(data) and data[left_child] < data[max_index]:
        max_index = left_child
    right_child = 2 * i + 2
    if right_child < len(data) and data[right_child] < data[max_index]:
        max_index = right_child

    if i != max_index:
        data[i], data[max_index] = data[max_index], data[i]
        swaps.append((i, max_index))
        sift_down(data, max_index, swaps)


def build_heap(data):
    swaps = []
    for i in range(len(data) // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
