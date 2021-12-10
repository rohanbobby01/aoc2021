def remove(li, i):
    return li[:i] + li[i + 2:]


def indices_to_remove(li, ind):
    for i in range(len(li) - 1):
        val = li[i] + li[i + 1]
        a, r, cr, sq = '<>', '()', '{}', '[]'
        if val == a or val == r or val == cr or val == sq:
            ind.append(i)
    return ind


with open('data.txt', 'r') as file:
    ans1 = 0
    em_list = []
    my_list = file.read().split()
    for j in range(len(my_list)):
        new_s = my_list[j]
        i = indices_to_remove(my_list[j], [])
        while len(i) != 0:
            i = indices_to_remove(my_list[j], [])
            i.reverse()
            for a in i:
                my_list[j] = remove(my_list[j], a)
        if new_s == my_list[j]:
            continue
        else:
            for val in my_list[j]:
                if val == ')':
                    ans1 += 3
                    break
                elif val == ']':
                    ans1 += 57
                    break
                elif val == '}':
                    ans1 += 1197
                    break
                elif val == '>':
                    ans1 += 25137
                    break
    for item in my_list:
        if ')' not in item and ']' not in item and '}' not in item and '>' not in item:
            total = 0
            for b in item[::-1]:
                if b == '(':
                    total = 5 * total + 1
                elif b == '[':
                    total = 5 * total + 2
                elif b == '{':
                    total = 5 * total + 3
                elif b == '<':
                    total = 5 * total + 4
            em_list.append(total)

    em_list.sort()
    ans2 = em_list[int(len(em_list)/2)]
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
