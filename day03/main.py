def sum_i(li, index):
    total = 0
    for element in li:
        total += int(element[index])
    return total


def remove_0(li, index):
    em = []
    for elements in li:
        if int(elements[index]) == 1:
            em.append(elements)
    return em


def remove_1(li, index):
    em = []
    for elements in li:
        if int(elements[index]) == 0:
            em.append(elements)
    return em


def bin_to_num(s):
    value = 0
    for index, nm in enumerate(s):
        if int(nm) == 1:
            value += 2 ** (11 - index)
    return value


with open('data.txt', 'r') as file:
    gamma = []
    eps = []
    g_num = 0
    e_num = 0
    my_list = file.read().splitlines()

    for i in range(12):
        if sum_i(my_list, i) > 500:
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
