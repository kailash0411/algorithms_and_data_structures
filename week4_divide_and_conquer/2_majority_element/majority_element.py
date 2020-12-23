# Uses python3
import sys


def get_majority_element_non_divide_and_conquer(a, n):
    count = {}
    for element in a:
        count[element] = 0
    for element in a:
        count[element] = count[element] + 1
        if count[element] > int(n / 2):
            return 1
    return 0

def get_majority_element(a, left, right):
    print('inside get majority')
    print(" left " + str(left) + " right " + str(right))
    if left + 1 == right:
        return [[a[left]], []]

    mid = int(left + (right - left) / 2)
    print("mid " + str(mid))
    left_half = get_majority_element(a, left, mid)
    print("left half " + str(left_half))
    right_half = get_majority_element(a, mid, right)
    print("right half " + str(right_half))
    return count_merge(left_half, right_half)

def count_merge(left_half, right_half):
    print("inside count_merge")
    [left_majors, right_minors] = chunk_process(left_half[0], right_half[1])
    [right_majors, left_minors] = chunk_process(right_half[0], left_half[1])
    if left_majors[0] == right_majors[0]:
        return [left_majors + right_majors, left_minors + right_minors]
    elif len(left_majors) > len(right_majors):
        return [left_majors, right_majors + left_minors + right_minors]
    else:
        return [right_majors, left_majors + right_minors + left_minors]

def chunk_process(majors, eles):
    print("inside chunk process")
    left = []
    for ele in eles:
        if majors[0] == ele:
            majors.append(ele)
        else:
            left.append(ele)
    print([majors, left])
    return [majors, left]


if __name__ == '__main__':
    # input = sys.stdin.read()
    n, *a = list(map(int, input().split()))
    print(get_majority_element_non_divide_and_conquer(a, n))