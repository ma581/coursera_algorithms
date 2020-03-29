def quicksort(input):
    print(f'QuickSorting {input} *************')
    if len(input) <= 1:
        return input, 0
    else:
        pivot_index, pivot_value = choose_pivot(input)
        partitioned, count = partition(input, pivot_index, pivot_value)

        if len(input) > 2:
            new_pivot_index = partitioned.index(pivot_value)
            left = partitioned[0: max(new_pivot_index, 1)]
            right = partitioned[max(new_pivot_index, 1):]

            sorted_left, count_left = quicksort(left)
            sorted_right, count_right = quicksort(right)
            return sorted_left + sorted_right, count + count_left + count_right
        else:
            return partitioned, count


def partition(_input, pivot_index, pivot_value):
    input = _input.copy()
    if len(input) < 2:
        return input, 0
    else:
        swap(input, 0, pivot_index)
        l = 1
        for j in range(l, len(input)):
            if input[j] < pivot_value:
                swap(input, l, j)
                l += 1
        # if i > 1:
        swap(input, 0, l - 1)
        print(f'Partition result: {input}')
        return input, len(input) - 1


def choose_pivot(input):
    print(f'Choosing pivot for {input} to be {input[0]}')
    return 0, input[0]


def swap(input, i, j):
    print(f'{input} Swapping {input[i]}, {input[j]}')
    temp = input[i]
    input[i] = input[j]
    input[j] = temp


def test_should_sort_sorted():
    input = [3, 5]
    sorted, count = quicksort(input)
    assert sorted == [3, 5]
    assert count == 1


def test_should_sort_simplest():
    input = [5, 3]
    sorted, count = quicksort(input)
    assert sorted == [3, 5]
    assert count == 1


def test_should_sort_array_of_size_three():
    input = [5, 6, 3]
    sorted, count = quicksort(input)
    assert sorted == [3, 5, 6]
    assert count == 3


def test_should_sort_array_of_size_three_again():
    input = [3, 5, 6]
    sorted, count = quicksort(input)
    assert sorted == [3, 5, 6]
    assert count == 3


def test_should_sort_with_pivot_largest():
    input = [3, 2, 1]
    sorted, count = quicksort(input)
    assert sorted == [1, 2, 3]
    assert count == 3


def test_should_sort_large_array():
    input = [5, 1, 2, 6]
    sorted, count = quicksort(input)
    assert sorted == [1, 2, 5, 6]
    assert count == 5
