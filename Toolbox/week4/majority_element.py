def majority_element_boyer_moore(elements):
    candidate = None
    count = 0

    for e in elements:
        if count == 0:
            candidate = e
            count = 1
        elif candidate == e:
            count += 1
        else:
            count -= 1

    count = elements.count(candidate)
    if count > len(elements) / 2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_boyer_moore(input_elements))
