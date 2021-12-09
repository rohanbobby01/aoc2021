def h_range(arr, x, y):
    max_x = len(arr[y]) - 1
    minx_x = 0
    for j in range(x, len(arr[y])):
        if arr[y][j] == 9:
            max_x = j - 1
            break
    for j in range(x, -1, -1):
        if arr[y][j] == 9:
            minx_x = j + 1
            break
    return range(minx_x, max_x + 1)


def v_range(arr, y, x):
    max_y = len(arr) - 1
    min_y = 0
    for i in range(y, len(arr)):
        if arr[i][x] == 9:
            max_y = i - 1
            break
    for i in range(y, -1, -1):
        if arr[i][x] == 9:
            min_y = i + 1
            break
    return range(min_y, max_y + 1)


def complex_fn(li, i, j, new_list):
    for a in v_range(li, i, j):
        for b in h_range(li, j, a):
            new_list.append((a, b))
    for a in h_range(li, j, i):
        for b in v_range(li, i, a):
            new_list.append((b, a))


def str_to_list(s):
    em_list = []
    for a in s:
        em_list.append(int(a))
    return em_list


with open('data.txt', 'r') as file:
    li = list(map(lambda x: str_to_list(x), file.read().split()))
    ans1 = 0
    em = []
    for i in range(len(li)):
        for j in range(len(li[i])):
            new_list = []
            another_list = []
            count = 0
            try:
                if li[i][j] < li[i + 1][j]:
                    count += 1
            except IndexError:
                count += 1
            try:
                1 / i
                if li[i][j] < li[i - 1][j]:
                    count += 1
            except ZeroDivisionError:
                count += 1
            try:
                if li[i][j] < li[i][j + 1]:
                    count += 1
            except IndexError:
                count += 1
            try:
                1 / j
                if li[i][j] < li[i][j - 1]:
                    count += 1
            except ZeroDivisionError:
                count += 1
            if count == 4:
                ans1 += li[i][j] + 1
                complex_fn(li, i, j, new_list)
                for x, y in set(new_list):
                    complex_fn(li, x, y, another_list)
                em.append(len(set(another_list)))

    em.sort()
    ans2 = em[-1] * em[-2] * em[-3]
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
