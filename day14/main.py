import string


def convert(upd_d, i_s):
    d = dict.fromkeys(string.ascii_uppercase, 0)
    for k, v in upd_d.items():
        d[k[0]] += v
        d[k[1]] += v
    d[i_s[0]] += 1
    d[i_s[-1]] += 1
    d = {x: y for x, y in d.items() if y != 0}
    return int((max(d.values()) - min(d.values())) / 2)


def update(upd_d, conv_d, i_zeros):
    for k, v in upd_d.items():
        i_zeros[k[0] + conv_d[k]] += v
        i_zeros[conv_d[k] + k[1]] += v
    return i_zeros


with open('data.txt', 'r') as file:
    li = list(map(lambda x: x.strip(), file.readlines()))
    inp_str = li[0]
    conversion = list(map(lambda x: x.split(' -> '), li[2:]))
    conv_dict = {}
    upd_dict = {}
    for a, b in conversion:
        conv_dict.update({a: b})
        upd_dict.update({a: 0})
    in_zeros = upd_dict.copy()
    for i in range(len(inp_str) - 1):
        total = inp_str[i] + inp_str[i + 1]
        upd_dict[total] += 1
    for i in range(40):
        upd_dict = update(upd_dict, conv_dict, in_zeros.copy())
        if i == 9:
            ans1 = convert(upd_dict, inp_str)
    ans2 = convert(upd_dict, inp_str)
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
