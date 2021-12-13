import numpy as np


def x_fold(ar, x):
    x1 = ar[:, :x]
    r1, c1 = x1.shape
    x2 = ar[:, x + 1:][:, ::-1]
    r2, c2 = x2.shape
    return np.hstack((np.zeros((r1, c1 - c2)), x2)) + x1


def y_fold(ar, y):
    y1 = ar[:y, :]
    r1, c1 = y1.shape
    y2 = ar[y + 1:, :][::-1, :]
    r2, c2 = y2.shape
    return np.vstack((np.zeros((r1 - r2, c1)), y2)) + y1


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
