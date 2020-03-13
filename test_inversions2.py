import math


def count_inversions(input):
    length = len(input)
    if length == 2:
        if input[1] < input[0]:
            return 1
        else:
            return 0
    elif length == 1:
        return 0
    else:
        half_way = math.floor(length // 2)
        left_inversions = count_inversions(input[0:half_way])
        right_inversions = count_inversions(input[half_way:length])
        split = split_inversions(input)
        print(f'Left: {left_inversions}, Right: {right_inversions}, Merge: {split}')
        return left_inversions + right_inversions + split


def split_inversions(input):
    (sorted, count) = merge_sort(input, 0)
    return count


def merge_sort(input, count):
    length = len(input)
    if length == 2:
        if input[0] <= input[1]:
            return input, 0
        else:
            return [input[1], input[0]], 0
    elif length == 1:
        return input, 0
    else:
        left, left_count = merge_sort(input[0:length // 2], 0)
        right, right_count = merge_sort(input[length // 2: length], 0)
        return merge(left, right, count)


def merge(left, right, count):
    sorted = []
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
                    count = count + 1
            else:
                sorted = sorted + left[i:]
                print(sorted)
                reached_end = True
        else:
            sorted = sorted + right[j:]
            print(sorted)
            reached_end = True

    return sorted, count


def test_should_find_one_left_inversion():
    input = [2, 1]
    assert count_inversions(input) == 1


def test_should_find_zero():
    input = [1, 2]
    assert count_inversions(input) == 0


def test_should_find_one_left_inversion_in_larger_array():
    input = [2, 1, 3, 4]
    assert count_inversions(input) == 1


def test_should_find_one_right_inversion_in_larger_array():
    input = [1, 2, 4, 3]
    assert count_inversions(input) == 1


def test_should_find_one_left_inversion_in_largest_array():
    input = [2, 1, 3, 4, 5, 6, 7, 8]
    assert count_inversions(input) == 1


def test_should_find_one_right_inversion_in_largest_array():
    input = [1, 2, 3, 4, 5, 6, 8, 7]
    assert count_inversions(input) == 1


def test_should_find_one_split_inversion():
    input = [1, 4, 3, 5]
    assert count_inversions(input) == 1


def test_should_merge():
    expected = [1, 2, 3, 4], 1
    left = [1, 3]
    right = [2, 4]
    assert merge(left, right, 0) == expected


def test_should_find_two_right_inversion_in_largest_array():
    input = [1, 2, 3, 4, 5, 8, 6, 7]
    assert count_inversions(input) == 2


def test_should_find_one_inversion_odd_size_array():
    input = [1, 3, 2]
    assert count_inversions(input) == 1


def test_should_find_17_inversions():
    input = [1, 5, 4, 8, 10, 2, 6, 9, 3, 7]
    assert count_inversions(input) == 17
