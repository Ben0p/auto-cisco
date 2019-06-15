from steps import autonomous, boot, configuration, details, enable, finalize, interface, login, test, version, parameters, config
from commands import close, com, credentials, initialize, match, read, write



"""
Main run file
"""



def main():

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
        configured, configured_as = configuration.check(console)

        # Set interface as set if already configured
        if configured:
            interface_set = True
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
                enabled = enable.check(console)
                configs_loaded = configuration.copy(console, vehicle)
                configure_command = configuration.command(console, vehicle)
                configured, configured_as = configuration.check(console)


        if configured:
            if configured_as == 'command':
                test_ok = test.command(console)
        
                if test_ok:
                    finalize.finish(console, vehicle)
                else:
                    print("Ping test failed")



if __name__ == '__main__':
    main()