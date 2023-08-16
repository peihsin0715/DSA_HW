def max_pairwise_product(numbers):
    n = len(numbers)
    #先算最大跟第二大的數字，這樣比較有效率（相較於把每個數字相乘再比較）
    max1 = -1
    max2 = -1
    for num in numbers:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
            
    max_product = max1 * max2

    return max_product

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

