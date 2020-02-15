import sys, math


def permutation(input, index):
    result = []
    insert_sequence = [index % x for x in range(1,len(input)+1)]
    i = 0
    for insert_index in insert_sequence:
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


if __name__ == "__main__":
    input = sys.argv[1]
    i = 0
    for p in permutations_generator(input):
        print(i, p)
        i += 1
