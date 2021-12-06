def dict_update(di):
    for k, v in di.items():
        if k == 0:
            di.update({9: di[9] + v})
            di.update(({7: di[7] + v}))
        else:
            di.update({k - 1: v})
            di.update({k: 0})


def list_to_dict(li, di):
    for a in range(10):
        di.update({a: 0})
    for item in li:
        di.update({item: li.count(item)})
    return di


with open('data.txt', 'r') as file:
    my_list = list(map(int, file.readline().split(',')))
    my_dict = list_to_dict(my_list, {})
    for i in range(256):
        if i == 80:
            ans1 = sum(my_dict.values())
        dict_update(my_dict)
    ans2 = sum(my_dict.values())
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
