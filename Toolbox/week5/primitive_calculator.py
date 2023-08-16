def compute_operations(n):
    min_operations = [float("inf")] * (n + 1)
    min_operations[0:2] = 0, 0
    prev = [0] * (n + 1)
    
    for i in range(2, n + 1):
        temp_2 = float("inf")
        temp_3 = float("inf")
        
        if i % 3 == 0:
            temp_3 = min_operations[i // 3]
        
        if i % 2 == 0:
            temp_2 = min_operations[i // 2]
        
        min_operations[i] = min(min_operations[i - 1], temp_2, temp_3) + 1
        
        if min_operations[i] == temp_3 + 1:
            prev[i] = i // 3
        elif min_operations[i] == temp_2 + 1:
            prev[i] = i // 2
        else:
            prev[i] = i - 1
    
    sequence = [n]
    i = n
    while i > 1:
        prev_number = prev[i]
        sequence.append(prev_number)
        i = prev_number
    
    sequence.sort()
    return sequence


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
