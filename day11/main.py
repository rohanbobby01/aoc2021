import numpy as np


def find_greater_than_9(ar, ind):
    for a in range(10):
        for b in range(10):
            if ar[a][b] > 9:
                ind.append((a, b))
    return ind


def add_adj_one(ar, pos):
    target = [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for x, y in target:
        if 0 <= pos[0] + x < 10 and 0 <= pos[1] + y < 10:
            ar[pos[0] + x][pos[1] + y] += 1
    ar[pos[0]][pos[1]] = 0


with open('data.txt', 'r') as file:
    my_list = file.read().split()
    arr = []
    for item in my_list:
        li = []
        for num in item:
            li.append(int(num))
        arr.append(li)
    np_arr = np.array(arr)
    total = 0
    ans2 = 0
    while True:
        em = []
        np_arr += 1
        while len(find_greater_than_9(np_arr, [])):
            i = find_greater_than_9(np_arr, [])
            for item in i:
                em.append(item)
                add_adj_one(np_arr, item)
        total += len(em)
        for val in em:
            np_arr[val[0]][val[1]] = 0
        if ans2 == 99:
            ans1 = total
        check = np_arr == np.zeros(10)
        ans2 += 1
        if check.all():
            break
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
