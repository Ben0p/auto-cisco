import os
import time

'''
Generates folders and config files for each device in lists
'''





def openConfig(config_in):
    with open(config_in) as ci:
        config = ci.read()
        ci.close()
    return(config)

def main():
    fleet_config = openConfig('./configs/templates/fleet')
    command_config = openConfig('./configs/templates/command')
    folder_all = './configs/all'

    with open('./lists/master.csv', 'r') as master:
        for row in master:
            stripped_row = row.strip()
            split_row = row.split(',')
            vehicle = split_row[0]
            command_ip = split_row[1]
            fleet_ip = split_row[2]
            fleet_hostname = 'cb-{}-fleet'.format(vehicle)
            command_hostname = 'cb-{}-command'.format(vehicle)

            # Folder
            folder_out = './configs/folders/{}'.format(vehicle)

            # Files
            fleet_file = '{}/cb-{}-fleet.txt'.format(folder_out, vehicle)
            command_file = '{}/cb-{}-command.txt'.format(folder_out, vehicle)
            fleet_all = './configs/all/cb-{}-fleet.txt'.format(vehicle)
            command_all = './configs/all/cb-{}-command.txt'.format(vehicle)

            # Generate configs
            new_fleet = fleet_config.format(hostname=fleet_hostname, ip=fleet_ip)
            new_command = command_config.format(hostname=command_hostname, ip=command_ip)

            # Create vehicle folder
            if not os.path.exists(folder_out):
                os.makedirs(folder_out)

            # Fleet config in folder
            with open(fleet_file, 'w') as ff:
                ff.write(new_fleet)
                ff.close()

            # Command config in folder
            with open(command_file, 'w') as cf:
                cf.write(new_command)
                cf.close()

            # Fleet in all folder
            with open(fleet_all, 'w') as fa:
                fa.write(new_fleet)
                fa.close() 
            
            # Command in all folder
            with open(command_all, 'w') as ca:
                ca.write(new_command)
                ca.close()     
            
            


if __name__ == '__main__':
    main()
