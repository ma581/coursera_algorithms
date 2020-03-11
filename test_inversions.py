# f = open('IntegerArray.txt', 'r')
# array_of_strings = f.read().splitlines()
# f.close()
#
# input_array = list(map(lambda x: int(x), array_of_strings))


def count_inversions(input):
    length = len(input)
    print(f'Counting inversions in {input}')
    if length == 2:
        return 1 if input[0] > input[1] else 0
    else:
        left = input[0:length // 2]
        right = input[length // 2: length]
        sorted, split_count = enhanced_merge_sort(left, right, 0)
        return count_inversions(left) + count_inversions(right) + split_count


def enhanced_merge_sort(a, b, count):
    print(f'sorting  {a}, {b}')
    length = len(a)
    if length == 1:
        if a[0] <= b[0]:
            return [a.pop(), b.pop()], 0
        else:
            return [b.pop(), a.pop()], 0
    else:
        a_l = a[0:length // 2]
        a_r = a[length // 2: length]

        b_l = b[0:length // 2]
        b_r = b[length // 2: length]

        sorted_a, count_a = enhanced_merge_sort(a_l, a_r, 0)
        sorted_b, count_b = enhanced_merge_sort(b_l, b_r, 0)
        return merge(sorted_a, sorted_b, count_a + count_b)


def merge(l, r, count):
    print(f'merging l: {l} and r:{r}')
    length_of_merged = len(l) * 2
    merged = [None] * length_of_merged
    for k in range(0, length_of_merged):
        # print(f'current merged: {merged}')
        if l:
            if r:
                if l[0] == r[0]:
                    merged[k:k + 1] = l.pop(0), r.pop(0)
                if l[0] < r[0]:
                    merged[k] = l.pop(0)
                else:
                    count = count + 1
                    merged[k] = r.pop(0)
            else:
                merged[k:length_of_merged] = l
                break
        else:
            merged[k:length_of_merged] = r
            break
    return merged, count


def test_should_sort_list():
    sorted, inversions = enhanced_merge_sort([1, 2, ], [4, 3], 0)
    assert sorted == [1, 2, 3, 4]


def test_should_sort_larger_list():
    sorted, inversions = enhanced_merge_sort([1, 2, 4, 3, ], [8, 7, 9, 6], 0)
    assert sorted == [1, 2, 3, 4, 6, 7, 8, 9]


def test_should_find_one_inversion():
    input = [1, 2, 4, 3]
    assert count_inversions(input) == 1


def test_should_find_three_inversion():
    input = [3, 2, 4, 1]
    assert count_inversions(input) == 3


def test_should_find_two_split_inversions():
    input = [1, 4, 2, 3]
    assert count_inversions(input) == 2


def test_should_find_three_split_inversions():
    input = [2, 4, 1, 3, 5, 6, 7, 8]
    assert count_inversions(input) == 3


def test_should_find_0_inversions():
    input = [1, 2, 3, 4, 5, 6, 7, 8]
    assert count_inversions(input) == 0


def test_should_find_1_inversion():
    input = [1, 2, 3, 4, 5, 6, 8, 7]
    assert count_inversions(input) == 1


def test_should_find_1_split_inversion():
    input = [1, 2, 3, 5, 4, 6, 7, 9]
    assert count_inversions(input) == 1


def test_should_find_4_split_inversions():
    input = [1, 2, 5, 6, 3, 4, 7, 9]
    assert count_inversions(input) == 4
