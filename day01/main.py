with open('data.txt','r') as file:
    my_list = file.readlines()
    total1 = 0
    for i in range(1999):
        if int(my_list[i+1]) > int(my_list[i]):
            total1 += 1
    total2 = 0
    for i in range(1997):
        if int(my_list[i+3]) > int(my_list[i]):
            total2 += 1
    print(f'Answer for problem 1:{total1}\nAnswer for problem 2:{total2}')






