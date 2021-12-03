def fn(li):
    new_list = [0] * len(li[0])
    for item in li:
        for i, num in enumerate(item):
            temp = new_list[i]
            new_list.pop(i)
            new_list.insert(i, temp + int(num))
    return new_list


def sum_i(li, i):
    total = 0
    for item in li:
        total += int(item[i])
    return total


def remove_0(li, i):
    em = []
    for item in li:
        if int(item[i]) == 1:
            em.append(item)
    return em


def remove_1(li, i):
    em = []
    for item in li:
        if int(item[i]) == 0:
            em.append(item)
    return em


def bin_to_num(s):
    value = 0
    for i, num in enumerate(s):
        if int(num) == 1:
            value += 2 ** (11 - i)
    return value


with open('data.txt', 'r') as file:
    gamma = []
    eps = []
    g_num = 0
    e_num = 0
    my_list = file.read().splitlines()
    for i, item in enumerate(fn(my_list)):
        if item > 500:
            g_num += 2 ** (11 - i)
        else:
            e_num += 2 ** (11 - i)
    ans1 = g_num * e_num
    new_list = my_list[:]
    for num in range(12):
        if sum_i(my_list, num) > len(my_list) / 2:
            my_list = remove_0(my_list, num)
        elif sum_i(my_list, num) < len(my_list) / 2:
            my_list = remove_1(my_list, num)
        else:
            my_list = remove_0(my_list, num)
    for num in range(12):
        if sum_i(new_list, num) < len(new_list) / 2 and sum_i(new_list, num) != 0:
            new_list = remove_0(new_list, num)
        elif sum_i(new_list, num) > len(new_list) / 2 and sum_i(new_list, num) != len(new_list):
            new_list = remove_1(new_list, num)
        elif sum_i(new_list, num) == len(new_list) / 2:
            new_list = remove_1(new_list, num)
    ans2 = bin_to_num(my_list[0])*bin_to_num(new_list[0])
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
