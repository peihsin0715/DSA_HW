from collections import deque

def max_sliding_window(sequence, m):
    max_values = []
    window = deque()

    for i in range(len(sequence)):
        # 移除窗口外的元素
        while window and window[0] <= i - m:
            window.popleft()
        
        # 從窗口右側移除所有小於等於當前元素的值
        while window and sequence[window[-1]] <= sequence[i]:
            window.pop()

        window.append(i)

        # 窗口大小達到 m 時，開始記錄最大值
        if i >= m - 1:
            max_values.append(sequence[window[0]])

    return max_values

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))
