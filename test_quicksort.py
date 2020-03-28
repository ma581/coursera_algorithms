def quicksort(input):
    # print(f'Sorting {input}')
    if input:
        pivot_index, pivot_value = choose_pivot(input)
        count = partition(input, pivot_index)

        if len(input) <= 2:
            return count
        else:
            pivot_position = input.index(pivot_value)
            left = input[0: pivot_position]
            right = input[pivot_position + 1:]
            # print(f'Left: {left}, Right {right}')

            count += quicksort(left)
            count += quicksort(right)
            return count
    else:
        return 0


def choose_pivot(input):
    return 0, input[0]


def partition(input, pivot_index):
    pivot_value = input[pivot_index]
    swap(input, 0, pivot_index)

    i = 0
    for j in range(1, len(input)):
        if input[j] <= pivot_value:
            swap(input, i + 1, j)
            # print(f'Swap result: {input}')
            i += 1

    swap(input, 0, max(i, 0))
    # print(f'Partition result: {input}')
    return len(input) - 1


def swap(input, i, j):
    # print(f'Input: {input} Swapping {input[i]}, {input[j]}')
    temp = input[i]
    input[i] = input[j]
    input[j] = temp


def test_should_sort_simplest():
    input = [5, 3]
    expected = ([3, 5], 1)
    count = quicksort(input)
    assert (input, count) == expected


def test_should_sort_sorted():
    input = [3, 5]
    expected = ([3, 5], 1)
    count = quicksort(input)
    assert (input, count) == expected


def test_should_sort_array_of_size_three():
    input = [5, 6, 3]
    expected = ([3, 5, 6], 2)
    count = quicksort(input)
    assert (input, count) == expected


def test_should_sort_array_of_size_three_again():
    input = [3, 5, 6]
    expected = ([3, 5, 6], 3)
    count = quicksort(input)
    assert (input, count) == expected


def test_should_sort_with_pivot_largest():
    input = [3, 2, 1]
    expected = ([1, 2, 3], 3)
    count = quicksort(input)
    assert (input, count) == expected
