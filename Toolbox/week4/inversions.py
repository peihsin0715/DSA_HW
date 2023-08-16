def merge_sort_and_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_inversions = merge_sort_and_count_inversions(arr[:mid])
    right, right_inversions = merge_sort_and_count_inversions(arr[mid:])
    merged, merge_inversions = merge_and_count_split_inversions(left, right)

    total_inversions = left_inversions + right_inversions + merge_inversions
    return merged, total_inversions

def merge_and_count_split_inversions(left, right):
    merged = []
    inversions = 0
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inversions

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n

    _, inversions = merge_sort_and_count_inversions(elements)
    print(inversions)
