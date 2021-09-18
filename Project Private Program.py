def greeting():
    name = input('> What is your name? : ')
    print(f"Hello {name}, Welcome to Private program")


def yourage():
    year = 2020
    try:
        born = int(input("when are you born : "))
    except ValueError:
        print("Invalid value")
    result = year - born
    print(f'Your age is : {result}')


def grade():
    ip = [3.65, 3.78, 3.80, 4.00, 3.90, 3.85, 3.75]
    semester = input('What semester do you wanna see ? : ')
    if semester == '1':
        print(f'Your grade in semester 1 is : {ip[0]}')
    elif semester == '2':
        print(f'Your grade in semester 2 is : {ip[1]}')
    elif semester == '3':
        print(f'Your grade in semester 3 is : {ip[2]}')
    elif semester == '4':
        print(f'Your grade in semester 4 is : {ip[3]}')
    elif semester == '5':
        print(f'Your grade in semester 5 is : {ip[4]}')
    elif semester == '6':
        print(f'Your grade in semester 6 is : {ip[5]}')
    elif semester == '7':
        print(f'Your grade in semester 7 is : {ip[6]}')


def password():
    your_password = input("Type your password here : ")
    print(f'Your password is {your_password}')


print('PRIVATE PROGRAM')
greeting()

while True:
    choose = input('> What do you wanna do? : ').lower()
    if choose == 'help':
        print(""" Here is what we can do :
Press '1' to : Know your age
press '2' to : Know your grade
press '3' to : know your password
press '4' to : quit
        """)
    elif choose == '1':
        yourage()
    elif choose == '2':
        grade()
    elif choose == '3':
        password()
    elif choose == '4' or choose == 'quit':
        print("See you next time")
        break
    else :
        print("Type 'help' if you dont know what will you do")
