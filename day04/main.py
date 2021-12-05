def in_num_to_space(li, nm):
    for a in range(5):
        for b in range(5):
            if li[a][b] == nm:
                li[a].pop(b)
                li[a].insert(b, ' ')


def check_row_space(li):
    count = 0
    for a in range(5):
        if li[a] == [' '] * 5:
            count += 1
    if count:
        return True


def check_particular_column_space(arr, ind):
    count = ''
    for a in range(5):
        count += arr[a][ind]
    if count == ' '*5:
        return True


def check_column_space(arr):
    for a in range(5):
        if check_particular_column_space(arr, a):
            return True


def check_arr(ar, in_num):
    for a in range(len(in_num)):
        for b in range(len(ar)):
            in_num_to_space(ar[b], in_num[a])
            if check_row_space(ar[b]) or check_column_space(ar[b]):
                return b, int(in_num[a])


def sum_arr(li):
    total = 0
    for a in range(5):
        for b in range(5):
            total += int(li[a][b].replace(' ', '0'))
    return total


with open('data.txt', 'r') as file:
    my_list = file.read().split("\n")
    input_num = my_list[0].split(',')
    data = list(filter(lambda x: x != '', my_list[1:]))
    arr2 = []
    arr3 = []
    for item in data:
        arr2.append(item.split())

    for i in range(100):
        arr3.append(arr2[0:5])
        arr2 = arr2[5:]
    for i in range(99):
        index, last = check_arr(arr3, input_num)
        if i == 0:
            ans1 = sum_arr(arr3[index])*last
        arr3.pop(index)
    index, last = check_arr(arr3, input_num)
    ans2 = sum_arr(arr3[index]) * last
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
