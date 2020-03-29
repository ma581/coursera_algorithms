def quicksort(input, choose_pivot):
    # print(f'QuickSorting {input} *************')
    if len(input) <= 1:
        return input, 0
    else:
        pivot_index, pivot_value = choose_pivot(input)
        # print(f'Chosen pivot={pivot_value}')
        partitioned, count = partition(input, pivot_index, pivot_value)

        if len(input) > 2:
            new_pivot_index = partitioned.index(pivot_value)
            left = partitioned[0: new_pivot_index]
            right = partitioned[new_pivot_index + 1:]

            sorted_left, count_left = quicksort(left, choose_pivot)
            sorted_right, count_right = quicksort(right, choose_pivot)
            return sorted_left + [pivot_value] + sorted_right, count + count_left + count_right
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
        swap(input, 0, l - 1)
        # print(f'Partition result: {input}')
        return input, len(input) - 1


def choose_first_value(input):
    # print(f'Choosing pivot for {input} to be {input[0]}')
    return 0, input[0]


def choose_last_value(input):
    # print(f'Choosing pivot for {input} to be {input[len(input) - 1]}')
    return len(input) - 1, input[len(input) - 1]


def choose_median_of_three(input):
    first = input[0]
    last = input[len(input) - 1]
    middle = input[(len(input) // 2) - 1]

    median = get_median(first, middle, last)
    return input.index(median), median


def get_median(first, middle, last):
    # print(f'Calculating median of {first}, {middle}, {last}')
    if last > middle > first or first > middle > last:
        return middle
    elif last > first > middle or middle > first > last:
        return first
    else:
        return last


def swap(input, i, j):
    # print(f'{input} Swapping {input[i]}, {input[j]}')
    temp = input[i]
    input[i] = input[j]
    input[j] = temp


def test_should_sort_sorted():
    input = [3, 5]
    sorted, count = quicksort(input, choose_first_value)
    assert sorted == [3, 5]
    assert count == 1


def test_should_sort_simplest():
    input = [5, 3]
    sorted, count = quicksort(input, choose_first_value)
    assert sorted == [3, 5]
    assert count == 1


def test_should_sort_array_of_size_three():
    input = [5, 6, 3]
    sorted, count = quicksort(input, choose_first_value)
    assert sorted == [3, 5, 6]
    assert count == 2


def test_should_sort_array_of_size_three_again():
    input = [3, 5, 6]
    sorted, count = quicksort(input, choose_first_value)
    assert sorted == [3, 5, 6]
    assert count == 3


def test_should_sort_with_pivot_largest():
    input = [3, 2, 1]
    sorted, count = quicksort(input, choose_median_of_three)
    assert sorted == [1, 2, 3]
    assert count == 3


def test_should_sort_large_array():
    input = [5, 1, 2, 6]
    sorted, count = quicksort(input, choose_median_of_three)
    assert sorted == [1, 2, 5, 6]
    assert count == 4

def test_should_pick_median_of_even_size_array():
    input = [8, 2, 4, 5, 7, 1]
    pivot_index, pivot_value = choose_median_of_three(input)
    assert pivot_value == 4
    assert pivot_index == 2


def test_should_pick_median_of_odd_size_array():
    input = [8, 2, 4]
    pivot_index, pivot_value = choose_median_of_three(input)
    assert pivot_value == 4
    assert pivot_index == 2


def test_should_pick_median_of_another_even_size_array():
    input = [4, 5, 6, 7]
    pivot_index, pivot_value = choose_median_of_three(input)
    assert pivot_value == 5
    assert pivot_index == 1


f = open('QuickSort.txt', 'r')
array_of_strings = f.read().splitlines()
f.close()
input_array = list(map(lambda x: int(x), array_of_strings))

# sorted_first, count_for_first = quicksort(input_array, choose_first_value)
# sorted_second, count_for_last = quicksort(input_array, choose_last_value)
sorted_third, count_for_median = quicksort(input_array, choose_median_of_three)

# print(count_for_first)
# print(count_for_last)
print(count_for_median)
