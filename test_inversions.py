import math


# f = open('IntegerArray.txt', 'r')
# array_of_strings = f.read().splitlines()
# f.close()
# input_array = list(map(lambda x: int(x), array_of_strings))
# print(f'Input array: {len(input_array)}')
# sorted, inversions = count_inversions(input_array)
# print(f'Total: {inversions}')

def count_inversions(input):
    length = len(input)
    if length == 2:
        if input[1] < input[0]:
            return [input[1], input[0]], 1
        else:
            return [input[0], input[1]], 0
    elif length == 1:
        return input, 0
    else:
        half_way = math.floor(length // 2)
        sorted_left, left_inversions = count_inversions(input[0:half_way])
        sorted_right, right_inversions = count_inversions(input[half_way:length])
        sorted, split = split_inversions(sorted_left + sorted_right)
        return sorted, left_inversions + right_inversions + split


def split_inversions(input):
    return merge_sort(input)


def merge_sort(input, count=0):
    length = len(input)
    if length == 2:
        if input[0] <= input[1]:
            return input, 0
        else:
            return [input[1], input[0]], 0
    elif length == 1:
        return input, 0
    else:
        left, left_count = merge_sort(input[0:length // 2])
        right, right_count = merge_sort(input[length // 2: length])
        return merge(left, right)


def merge(left, right):
    sorted = []
    count = 0
    reached_end = False
    i = 0
    j = 0
    while not reached_end:
        if i < len(left):
            if j < len(right):
                l = left[i]
                r = right[j]
                if l < r:
                    sorted.append(l)
                    i = i + 1
                else:
                    sorted.append(r)
                    j = j + 1
                    count = count + len(left[i:])
            else:
                sorted = sorted + left[i:]
                reached_end = True
        else:
            sorted = sorted + right[j:]
            reached_end = True
    return sorted, count


def test_should_find_one_left_inversion():
    input = [2, 1]
    sorted, inversions = count_inversions(input)
    assert inversions == 1


def test_should_find_zero():
    input = [1, 2]
    sorted, inversions = count_inversions(input)
    assert inversions == 0


def test_should_find_one_left_inversion_in_larger_array():
    input = [2, 1, 3, 4]
    sorted, inversions = count_inversions(input)
    assert inversions == 1


def test_should_find_one_right_inversion_in_larger_array():
    input = [1, 2, 4, 3]
    sorted, inversions = count_inversions(input)
    assert inversions == 1


def test_should_find_one_left_inversion_in_largest_array():
    input = [2, 1, 3, 4, 5, 6, 7, 8]
    sorted, inversions = count_inversions(input)
    assert inversions == 1


def test_should_find_one_right_inversion_in_largest_array():
    input = [1, 2, 3, 4, 5, 6, 8, 7]
    sorted, inversions = count_inversions(input)
    assert inversions == 1


def test_should_find_one_split_inversion():
    input = [1, 4, 3, 5]
    sorted, inversions = count_inversions(input)
    assert inversions == 1


def test_should_merge():
    expected = [1, 2, 3, 4], 1
    left = [1, 3]
    right = [2, 4]
    assert merge(left, right) == expected


def test_should_find_two_right_inversion_in_largest_array():
    input = [1, 2, 3, 4, 5, 8, 6, 7]
    sorted, inversions = count_inversions(input)
    assert inversions == 2


def test_should_find_one_inversion_odd_size_array():
    input = [1, 3, 2]
    sorted, inversions = count_inversions(input)
    assert inversions == 1


def test_should_find_17_inversions():
    input = [1, 5, 4, 8, 10, 2, 6, 9, 3, 7]
    sorted, inversions = count_inversions(input)
    assert inversions == 17
