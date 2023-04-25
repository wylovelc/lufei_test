accounts = {}
with open('user.db', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip().split(',')
        accounts[line[0]] = line


while True:
    username = input('请输入用户名：')

    if username not in accounts :
        print('用户不存在，请重新输入')
        continue
    else:
        if accounts[username][2] == '1':
            print('用户已经被锁定，请联系管理员')
            exit('bye....')
    count = 0
    while count < 3:
        password = input('请输入密码：')
        if password == accounts[username][1]:
            print('登录成功')
            exit('bye....')
        else:
            print('密码错误，请重新输入')
            count += 1

    with open('user.db', 'w', encoding='utf-8') as f:
        accounts[username][2] = '1'
        for line in accounts.values():
            f.write(','.join(line) + '\n')
        exit('bye....')