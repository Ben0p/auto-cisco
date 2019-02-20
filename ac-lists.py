

files = [
    ['./lists/in/lvs-in.csv', './lists/out/lvs.csv'],
    ['./lists/in/trucks-in.csv', './lists/out/trucks.csv'],
    ['./lists/in/cmd-in.csv', './lists/out/cmd.csv'],
    ['./lists/in/terrain-in.csv', './lists/out/terrain.csv'],
    ['./lists/in/support-in.csv', './lists/out/support.csv']
]

fleet_file = ['./lists/in/fleet-in.csv', './lists/out/fleet.csv']

master_list = './lists/master.csv'

def main():

    for _file in files:
        file_in = _file[0]
        file_out = _file[1]

        with open(file_out, 'w') as fo:

            with open(file_in, 'r') as fi:
                for line in fi:
                    split_line = line.split()

                    if len(split_line) == 5:
                        name = split_line[0]
                        ip = split_line[1]
                    
                        line_out = '{},{}\n'.format(name,ip)

                        fo.write(line_out)
                        print(line_out)
                fi.close()
            fo.close()
        
    with open(fleet_file[1], 'w') as ffo:
        with open(fleet_file[0], 'r') as ffi:
            for line in ffi:
                split_line = line.split()
                if len(split_line) > 5:
                    ip = split_line[-2]
                    name = split_line[-6]
                    line_out = '{},{}\n'.format(name,ip)
                    ffo.write(line_out)
                    print(line_out)
        ffi.close()
    ffo.close()
    







if __name__ == '__main__':
    main()