import numpy as np


def x_fold(ar, x):
    np_x1 = ar[:, :x]
    r, c = np_x1.shape
    np_x2 = ar[:, x + 1:]
    ar = np.zeros((r, c))
    for a in range(r):
        for b in range(0, x):
            ar[a][b] = np_x1[a][b] + np_x2[a][x - 1 - b]
    return ar


def y_fold(ar, y):
    np_x1 = ar[:y, :]
    r, c = np_x1.shape
    np_x2 = ar[y + 1:, :]
    ar = np.zeros((r, c))
    for a in range(0, y):
        for b in range(c):
            ar[a][b] = np_x1[a][b] + np_x2[y - 1 - a][b]
    return ar


def folding(ar, li):
    for val in li:
        if 'x' in val:
            ar = x_fold(ar, int(val.split('=')[1]))
            if val == li[0]:
                ans1 = np.count_nonzero(ar)
        else:
            ar = y_fold(ar, int(val.split('=')[1]))
    return ar, ans1


with open('data.txt', 'r') as file:
    pts = []
    folds = []
    for item in file.read().split('\n'):
        if ',' in item:
            pts.append(list(map(lambda num: int(num), item.split(','))))
        elif item != '':
            folds.append(item)
    x_max = max(list(map(lambda x: x[0], pts))) + 1
    y_max = max(list(map(lambda x: x[1], pts))) + 1
    np_ar = np.zeros((y_max, x_max))
    for x, y in pts:
        np_ar[y][x] = 1
    np_ar, ans1 = folding(np_ar, folds)
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:')
    for y in range(np_ar.shape[0]):
        for x in range(np_ar.shape[1]):
            if np_ar[y][x] > 0:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print('', end="\n")
