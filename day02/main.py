with open('data.txt', 'r') as file:
    my_list = file.readlines()
    aim = 0
    forward = 0
    down = 0
    down2 = 0
    for item in my_list:
        command = item.split(' ')[0]
        distance = int(item.split(' ')[1])
        if command == 'forward':
            forward += distance
            down2 += distance * aim
        elif command == 'down':
            down += distance
            aim += distance
        else:
            down -= distance
            aim -= distance
    ans1 = forward * down
    ans2 = forward * down2
    print(f'Answer for problem 1:{ans1}\nAnswer for problem 2:{ans2}')
