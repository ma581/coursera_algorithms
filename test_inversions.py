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
        return count_inversions(left) + count_inversions(right) + count_split_inversions(input)


def count_split_inversions(input):
    print(f'sorting  {input}')
    length = len(input)
    if length == 2:
        if input[0] <= input[1]:
            return input
        else:
            return [input[1], input[0]]
    else:
        left = input[0:length // 2]
        right = input[length // 2: length]
        split_count, merged = merge(count_split_inversions(left), count_split_inversions(right))
        print(f'merge: {merged}')
        return split_count


def merge(l, r):
    count = 0
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
    return count, merged


def test_should_find_one_inversion():
    input = [1, 2, 4, 3]  # 1 inversion
    assert count_inversions(input) == 1


def test_should_find_two_inversion():
    input = [3, 2, 4, 1]  # 3 inversion
    assert count_inversions(input) == 3


def test_should_find_split_inversion():
    input = [1, 4, 2, 3]  # 1 split inversion
    assert count_inversions(input) == 2

def test_should_find_split_inversions():
    input = [ 2, 4, 1, 3, 5, 6 ,7 ,8]  # 1 split inversion
    assert count_inversions(input) == 3

