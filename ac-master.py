


'''
Generates master list
'''

files = [
    ['./lists/in/lvs-in.csv', './lists/out/lvs.csv'],
    ['./lists/in/trucks-in.csv', './lists/out/trucks.csv'],
    ['./lists/in/cmd-in.csv', './lists/out/cmd.csv'],
    ['./lists/in/terrain-in.csv', './lists/out/terrain.csv'],
    ['./lists/in/support-in.csv', './lists/out/support.csv']
]

fleet_file = ['./lists/in/fleet-in.csv', './lists/out/fleet.csv']

master_list = './lists/master.csv'

master_array = []
unassigned = []


def attempt1():
    with open(master_list, 'a') as ml:
        print('Created blank master.csv')
        for _file in files:
            with open(fleet_file[1], 'r') as ff:
                print('Opened {}'.format(fleet_file[1]))
                with open(_file[1], 'r') as f:
                    print('Opened {}'.format(_file[1]))
                    for file_line in f:
                        for fleet_line in ff:
                            if file_line.split(',')[0] == fleet_line.split(',')[0]:
                                name = file_line.split(',')[0]
                                cmd_ip = file_line.split(',')[0]
                                fleet_ip = fleet_line.split(',')[0]
                                ml.write('{},{},{}\n'.format(name, cmd_ip, fleet_ip))
                                print('Matched {}'.format(name))
            ff.close()

def attempt2():
    for _file in files:
        with open(_file[1], 'r') as f:
            for line in f:
                stripped_line = line.strip()
                split_line = stripped_line.split(',')
                master_array.append([split_line[0], split_line[1]])
    with open(master_list, 'a') as ml:
        with open(fleet_file[1], 'r') as ff:
                for line in ff:
                    fleet_strip = line.strip()
                    fleet_split = fleet_strip.split(',')
                    fleet_name = fleet_split[0]
                    for device in master_array:
                        device_name = device[0]
                        if fleet_name == device_name:
                            cmd_ip = device[1]
                            fleet_ip = fleet_split[1]
                            ml.write('{},{},{}\n'.format(device_name, cmd_ip, fleet_ip))
                            print('Matched {}'.format(device_name))
                        else:
                            unassigned.append(device_name)
    with open('./lists/unassigned.csv', 'a') as ua:
        unassigned_set = set(unassigned)
        for item in unassigned_set:
            ua.write('{}\n'.format(item))

if __name__ == '__main__':
    attempt2()