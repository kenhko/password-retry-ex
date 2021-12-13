password = 'a123456'
i = 3

while i > 0:
    passwords = input ('Please input your password: ')
    if passwords == password:
        print ('Log In')
        break 
    else: 
        i = i - 1 
        print ('Wrong Password!')
        if i > 0:
            print('Still have' , i , 'changes')
        else:
            print('No more change, Locked account!')
            