import sys, math


def permutation(input, index):
    result, i = [], 0
    for insert_index in [index % x for x in range(1,len(input)+1)]:
        result.insert(insert_index, input[i])
        i += 1
    return result


def permutations_generator(input):
    if len(input) < 2:
        yield input
        return
    for sub_perm in permutations_generator(input[1:]):
        for i in range(len(input)):
            yield sub_perm[:i] + input[:1] + sub_perm[i:]


def combination_count(n, k):
    return int((math.factorial(n) / math.factorial(k)) / math.factorial(n - k))


def pascal_row(row):
    return [combination_count(row, col) for col in range(0, row+1)]


def pascal_triangle(rows):
    return [pascal_row(row) for row in range(0, rows)]


if __name__ == "__main__":
    input = sys.argv[1]
    i = 0
    for p in permutations_generator(input):
        print(i, p)
        i += 1

    #print(''.join(permutation(input, 10)))
