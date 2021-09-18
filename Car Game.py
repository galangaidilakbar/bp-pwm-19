command = ""
started = False
while True:
    command = input('> ').lower() 
    if command == 'start':
        if started:
            print('Car is already started')
        else :
            started = True
            print('Car started...')
    elif command == 'stop': 
        if not started:
            print('Car already stopped!')
        else:
            started = False
            print('Car stopped .')
        stop = True
    elif command == 'stop' and already == True :
        print('car already stop')
    elif command == 'quit' :
        break
    elif command == 'help' :
        print(
            """
start - to start the car
stop - to stop the car
quit - to quit

            """)
    else :
        print ("Sorry... i don't understands that, Please write Help to open the menu")