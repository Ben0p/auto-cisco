# auto-cisco
Automated Cisco 3702 configuration file generator and programmer

## Features
* Converts AP to autonomous
* Sets a temporary IP address on BVI1
* Uploads new firmware via tftp
* Uploads generated config via tftp
* Does a ping test
* Whole thing is looped for easy batching

## Steps

1. Parameters are stored in a settings.txt file
    * COM port
    * Temp IP address
    * PC IP address
    * Hostname prefix and suffix
    * Firmware file
    * Template file
2. settings.txt is populated with default settings if non existent
3. Does pre-flight checks
    * Config file
    * PC IP
    * Serial Port
    * Firmware file
    * TFTP is running
4. Prompts for a name
5. Looks up name against master.csv to retrieve IP address
6. Initialized serial COM port
7. Waits for 3702 to boot
8. Checks if autonomous
9. Checks firmware version
10. Checks configuration status
11. Does whatever needs to be done at this point