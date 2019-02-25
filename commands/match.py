


def boot(prompt):
    if len(prompt) > 9:
        if prompt[-7] == '-fleet>' or prompt[-7] == '-fleet#':
            return(True)
        if prompt[-9] == '-command>' or prompt[-9] == '-command#':
            return(True)
        elif prompt[:9] == 'Username:' or prompt[:9] == 'Password':
            return(True)
        elif len(prompt) == 17 and prompt[:2] == 'AP' and prompt[-1:] == '>':
            return(True)
        elif len(prompt) == 17 and prompt[:2] == 'AP' and prompt[-1:] == '#':
            return(True)
        elif prompt[:9] == ' --More--':
            return(True)
        else:
            return(False)
    else:
        if prompt == 'ap>' or prompt == 'ap#':
            return(True)
        else:
            return(False)