from steps import autonomous, boot, configuration, details, enable, finalize, interface, login, test, version, parameters, config
from commands import close, com, credentials, initialize, match, read, write
import time
import socket, errno



"""
Main run file
"""

def start():
    import tftpy
    server = tftpy.TftpServer('')
    server.listen('0.0.0.0', 69)

def launchTFTP():

    import multiprocessing
    multiprocessing.freeze_support()
    print("Launching tftp server")            
    t = multiprocessing.Process(target=start)
    t.daemon = True
    t.start()
    return(True)


def portInUse(port):
    import socket

    print(f"Checking if TFTP port {port} (nice) is available...")
    fail_count = 0
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            try:
                s.bind(('0.0.0.0', port))
                s.close()
                return(False)
            except:
                if fail_count >= 3:
                    print("Get your sh** together, put it in a bag and take it to the sh** store, just get it together...")
                    input("Check Task Manager for SolarWinds TFTP Sever, and yeet it")
                    fail_count = 0
                fail_count += 1
                input("Port is already in use, close running tftp server and press [E n t e rr] ")

def main():

    if not portInUse(69):
        launchTFTP()

    already_configured = False

    while True:
        # Get parameters
        params = parameters.get()

        # Get vehicle details
        vehicle = details.get()

        # Check config exists
        if not config.exists(vehicle):
            config.generate(vehicle)

        # Initialize serial
        console = initialize.port()

        # Check if finished booting, otherwise waits until done
        booted = boot.check(console)

        # Check autonomous status
        is_autonomous = autonomous.check(console)

        # Check upgrade status
        upgraded = version.check(console)

        # Check config
        configured = configuration.check(console)

        # Set interface as set if already configured
        if configured:
            interface_set = True
            already_configured = True
        elif not configured:
            interface_set = False

        # Login / convert to autonomous
        if not is_autonomous:
            logged_in = login.now(console)
            if logged_in:
                autonomous.convert(console)

            # Wait for boot
            booted = boot.check(console)
        

        if is_autonomous:
            enabled = enable.check(console)
            if not configured:
                interface_set = interface.check(console)
        
        if not interface_set:
            enabled = enable.check(console)
            interface_configured = interface.configure(console)
            interface_set = True

        if interface_set:
            if not upgraded:
                enabled = enable.check(console)
                upgraded = version.upgrade(console)
                booted = boot.check(console)
        
        if upgraded:
            if not configured:
                # Check if enabled
                enabled = enable.check(console)
                # Copy config, prompt if already exists
                configuration.copy(console, vehicle)
                # Loads config into running-config
                configuration.load(console, vehicle)
                # Checks if configured 
                configured = configuration.check(console)

        
        if already_configured:
            overwrite = configuration.overWrite()
            if overwrite:
                interface_configured = interface.check(console)
                if not interface_configured:
                    interface.configure(console)
                enabled = enable.check(console)
                configuration.copy(console, vehicle)
                configured = configuration.load(console, vehicle)

        test.command(console)
        finalize.finish(console, vehicle)




if __name__ == '__main__':


    main()