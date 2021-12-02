with open('data.txt', 'r') as file:
    my_list = file.readlines()
    total1 = 0
    total2 = 0
    for item in my_list:
        password = item.split(': ')[1]
        policy = item.split(': ')[0]
        policy_condition = policy.split(' ')[0]
        letter = policy.split(' ')[1]
        count = password.count(letter)
        if int(policy_condition.split('-')[0]) <= count <= int(policy_condition.split('-')[1]):
            total1 += 1
        first_letter = password[int(policy_condition.split('-')[0]) - 1]
        second_letter = password[int(policy_condition.split('-')[1]) - 1]
        letters_combined = first_letter + second_letter
        if letters_combined.count(letter) == 1:
            total2 += 1
    print(f'Answer for problem 1:{total1}\nAnswer for problem 2:{total2}')
