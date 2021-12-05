def points_with_count(my_dict, lis):
    for item in lis:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1


def hv_points_list(x1, y1, x2, y2, lis):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            lis.append((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            lis.append((x, y1))
    return lis


def hvd_points_list(x1, y1, x2, y2, lis):
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            lis.append((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            lis.append((x, y1))
    if abs(x2 - x1) == abs(y2 - y1):
        for i in range(abs(x2 - x1) + 1):
            if x1 + y1 == x2 + y2:
                lis.append((min(x1, x2) + i, max(y1, y2) - i))
            else:
                lis.append((min(x1, x2) + i, min(y1, y2) + i))
    return lis


with open('data.txt', 'r') as file:
    my_list = file.readlines()
    dict_1 = {}
    dict_2 = {}
    ans1 = 0
    ans2 = 0
    for i in my_list[:500]:
        a, b = i.split(' -> ')
        (x1, y1), (x2, y2) = (int(a.split(',')[0]), int(a.split(',')[1])), (int(b.split(',')[0]), int(b.split(',')[1]))
        hv_points = hv_points_list(x1, y1, x2, y2, [])
        points_with_count(dict_1, hv_points)
        hvd_points = hvd_points_list(x1, y1, x2, y2, [])
        points_with_count(dict_2, hvd_points)
    for key, value in dict_1.items():
        if value > 1:
            ans1 += 1
    for key, value in dict_2.items():
        if value > 1:
            ans2 += 1
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
