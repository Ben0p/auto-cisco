import os
import time

'''
Generates folders and config files for each device in lists
'''


<<<<<<< HEAD
files = [
    ['./configs/lvs', './lists/out/lvs.csv'],
    ['./configs/trucks', './lists/out/trucks.csv'],
    ['./configs/cmd', './lists/out/cmd.csv'],
    ['./configs/terrain', './lists/out/terrain.csv'],
    ['./configs/support', './lists/out/support.csv']
]


fleet_config =  '''{}'''.format(open('./configs/fleet', 'r').read())

def openConfig(config_in):
    with open(config_in) as ci:
        config = ci.read()
        ci.close()
    return(config)

def main():
    cmd_config = openConfig('./configs/command')
    fleet_config = openConfig('./configs/fleet')
    for _file in files:
        if not os.path.exists(_file[0]):
            os.makedirs(_file[0])
            print('Created directory {}'.format(_file[0]))
        with open(_file[1], 'r') as fi:
            for line in fi:
                name, ip = line.split(',')
                folder_out = '{}/{}'.format(_file[0],name)
                fleet_file = '{}/{}-fleet.txt'.format(folder_out, name)
                cmd_file = '{}/{}-command.txt'.format(folder_out, name)
                if not os.path.exists(folder_out):
                    os.makedirs(folder_out)
                    print('Created directory for {}'.format(name))
                fleet_hostname = '{}-fleet'.format(name)
                cmd_hostname = '{}-command'.format(name)
                new_fleet = fleet_config.format(hostname=fleet_hostname, ip=ip)
                new_cmd = cmd_config.format(hostname=cmd_hostname, ip=ip)
                with open(fleet_file, 'w') as ff:
                    ff.write(new_fleet)
                    ff.close()
                    print('Created fleet config for {}'.format(name))
                with open(cmd_file, 'w') as cf:
                    cf.write(new_cmd)
                    cf.close()
                    print('Created fleet config for {}'.format(name))



if __name__ == '__main__':
    main()
=======
'''
Generates folders and config files for each device from an input .csv
'''
>>>>>>> 01e41dc0a26a437aaa67ab0735663f68ce2f2052
