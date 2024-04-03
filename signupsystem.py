username=input('Enter your username: ')

password=input('Enter your password: ')

print('your account has been created successfully')

print('please login!')

username2=input('Enter your username: ')

password2=input('Enter your password: ')

if username==username2 and password==password2:
    print("login successful")
else:
    print("Wrong Username or Password!\nPlease try again.")