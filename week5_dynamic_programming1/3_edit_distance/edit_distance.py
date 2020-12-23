# Uses python3
def edit_distance(s, t):
    ed = [[x for x in range(len(s) + 1)] for y in range(len(t) + 1)]
    for y in range(len(t) + 1):
        ed[y][0] = y
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            del_op = ed[j][i-1] + 1
            insert_op = ed[j - 1][i] + 1
            mismatch = ed[j - 1][i - 1] + 1
            match = ed[j - 1][i- 1]
            if s[i - 1] == t[j - 1]:
                ed[j][i] = min(insert_op, del_op, match)
            else:
                ed[j][i] = min(insert_op, del_op, mismatch)

    return ed[len(t)][len(s)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
