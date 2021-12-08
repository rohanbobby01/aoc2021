def str_to_set(s):
    li = []
    for a in s:
        li.append(a)
    return set(li)


with open('data.txt', 'r') as file:
    my_list_1 = list(map(lambda x: x.split(" | ")[0].split(), file.readlines()))
with open('data.txt', 'r') as file:
    my_list_2 = list(map(lambda x: x.split(" | ")[1].split(), file.readlines()))
    ##################################Part One##################################
    ans1 = 0
    for i in range(len(my_list_1)):
        my_dict_1 = {}
        my_dict_2 = {2: 0, 4: 0, 3: 0, 7: 0}
        for item in my_list_1[i]:
            if len(item) in my_dict_1.keys():
                my_dict_1.update({len(item): my_dict_1[len(item)] + 1})
            else:
                my_dict_1.update({len(item): 1})
        for item in my_list_2[i]:
            if len(item) in my_dict_2.keys():
                my_dict_2.update({len(item): my_dict_2[len(item)] + 1})
            else:
                my_dict_2.update({len(item): 1})
        if my_dict_1[2]:
            ans1 += my_dict_2[2]
        if my_dict_1[3]:
            ans1 += my_dict_2[3]
        if my_dict_1[4]:
            ans1 += my_dict_2[4]
        if my_dict_1[7]:
            ans1 += my_dict_2[7]
    ##################################Part Two##################################
    ans2 = 0
    for i in range(len(my_list_1)):
        my_dict_1 = {}
        my_dict_2 = {}
        for item in my_list_1[i]:
            my_dict_1.update({len(item): item})
        my_str = ''
        for j in range(len(my_list_2[i])):
            if len(my_list_2[i][j]) == 5:
                if str_to_set(my_dict_1[2]).issubset(str_to_set(my_list_2[i][j])) or \
                        str_to_set(my_dict_1[3]).issubset(str_to_set(my_list_2[i][j])):
                    my_str += '3'
                elif len(str_to_set(my_dict_1[4]).symmetric_difference(str_to_set(my_list_2[i][j]))) == 3:
                    my_str += '5'
                else:
                    my_str += '2'
            elif len(my_list_2[i][j]) == 6:
                if str_to_set(my_dict_1[4]).issubset(str_to_set(my_list_2[i][j])):
                    my_str += '9'
                elif str_to_set(my_dict_1[3]).issubset(str_to_set(my_list_2[i][j])):
                    my_str += '0'
                else:
                    my_str += '6'
            elif len(my_list_2[i][j]) == 2:
                my_str += '1'
            elif len(my_list_2[i][j]) == 4:
                my_str += '4'
            elif len(my_list_2[i][j]) == 3:
                my_str += '7'
            else:
                my_str += '8'
        ans2 += int(my_str)
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
