import os
from steps import parameters

def check():
    '''
    Checks if /lists/master.csv exists
    '''

    if not os.path.isdir('lists'):
        print("No lists directory found, creating directry...")
        try:
            os.mkdir('lists')
        except OSError:
            print("Failed to create lists directory")
        else:  
            print("Created lists directory")

    while True:
        if not os.path.exists('lists/master.csv'):
            create = input("'lists/master.csv' not found, do you want to create a blank list? (y/n)")
            if create == 'y':
                try:
                    open('lists/master.csv', 'a').close()
                    print("Created 'lists/master.csv'")
                    return(True)
                except:
                    print("Failed to create 'lists/master.csv'")
                    return(False)
            if create == 'n':
                input("Copy master.csv into /lists/master.csv (format: [name,ip]) and press ENTER")
            else:
                print("Enter y or n")
        else:
            return(True)

def get(): 
    check()
    params = parameters.get()
    while True:
        no_match = True
        name = input("Enter vehicle name (e.g. DT201): ")
        hostname = '{}{}{}'.format(params['prefix'], name, params['suffix']).lower()
        with open('./lists/master.csv', 'r') as f:
            for line in f:
                stripped = line.strip()
                split = stripped.split(',')
                if split[0] == name:
                    print('-------- Matched --------')
                    print('    Name: {}'.format(split[0]))
                    print('Hostname: {}'.format(hostname))
                    print('      IP: {}'.format(split[1]))
                    print('-------------------------')
                    user_input = input('Is this correct? (y/n): ')
                    while True:
                        if user_input == 'y':
                            return(split)
                        elif user_input == 'n':
                            print("Try again...")
                            no_match = False
                            break
                        else:
                            user_input = input("Enter 'y' or 'n': ")

        if no_match:
            print("No match found in master.csv")
            appendage = input("Would you like to append (y) or try again (n): ")
            if appendage == 'y':
                ip = input("Enter IP address: ")
                print("------------------")
                print("    Name: {}".format(name))
                print("Hostname: {}".format(hostname))
                print("      IP: {}".format(ip))
                print("------------------")
                check_append = input("You good bro? (y/n): ")
                if check_append == 'y':
                    append(name, ip)
                    print("Appended {} to master.csv".format(name))
                    return(name, ip)
                if check_append == 'n':
                    break
                else:
                    print("You gone and stuffed up, starting again...")
                    break
            if appendage == 'n':
                input("Fix up the spreadsheet and press ENTER to try again")
            else:
                print("Sort your shit out, starting again...")

def append(name, ip):
    with open('lists/master.csv', 'a') as f:
        f.write('{},{}\n'.format(name, ip))
        f.close


if __name__ == '__main__':
    os.chdir('..')
    get()
    
