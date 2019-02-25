

def get(): 

    while True:
        no_match = True
        name = input("Enter vehicle name (e.g. DT201): ")
        with open('./lists/master.csv', 'r') as f:
            for line in f:
                stripped = line.strip()
                split = stripped.split(',')
                if split[0] == name:
                    print('----- Matched {} -----'.format(split[0]))
                    print('  Fleet IP: {}'.format(split[2]))
                    print('Command IP: {}'.format(split[1]))
                    print('-------------------------')
                    user_input = input('Is this correct? (y/n): ')
                    while True:
                        if user_input == 'y':
                            print('!!! Power up IW3702 now !!!')
                            return(split)
                        elif user_input == 'n':
                            print("Try again...")
                            no_match = False
                            break
                        else:
                            user_input = input("Enter 'y' or 'n': ")

        if no_match:
            print("No match found in master.csv")
            
