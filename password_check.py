MIN_LENGTH = 2

password = input("Password: ")
while len(password) < MIN_LENGTH:
    print('Invalid Password!')
    password = input("Password: ")
print("*" * len(password))