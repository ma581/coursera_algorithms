def quicksort(input):
    pivot = choose_pivot(input)

    partioned, count = partition(input, pivot)

    return partioned, count


def choose_pivot(input):
    return 0


def partition(input, pivot_index):
    pivot_value = input[pivot_index]
    swap(input, 0, pivot_index)

    i = 0
    for j in range(1, len(input)):
        if input[j] <= pivot_value:
            swap(input, i, j)
            print(f'result: {input}')
            i += 1

    swap(input, 0, i - 1)
    return input, len(input) - 1


def swap(input, i, j):
    temp = input[i]
    input[i] = input[j]
    input[j] = temp


def test_should_sort_simplest():
    input = [5, 3]
    expected = [3, 5]
    assert quicksort(input) == (expected, 1)
