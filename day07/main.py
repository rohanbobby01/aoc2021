def sum_n(num):
    return num*(num+1)/2


with open('data.txt', 'r') as file:
    my_list = list(map(int, file.readline().split(',')))
    my_dict_1 = {}
    my_dict_2 = {}
    for i in range(min(my_list), max(my_list)+1):
        count_1 =0
        count_2 = 0
        for item in my_list:
            count_1 += abs((item-i))
            count_2 += sum_n(abs(item - i))
        my_dict_1.update({i: count_1})
        my_dict_2.update({i: count_2})
    ans1, ans2 = min(my_dict_1.values()), int(min(my_dict_2.values()))
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
