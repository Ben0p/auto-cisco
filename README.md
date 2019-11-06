# auto-cisco
Automated Cisco 3702 configuration file generator and programmer

## Features
* Built in tftp server
* Wizard on first run
* Converts AP to autonomous
* Sets a temporary IP address on BVI1
* Uploads new firmware via tftp
* Uploads generated config via tftp
* Checks current status of 3702
    * If already configured (prompts to over-write)
    * If already autonomous
    * If already firmware updated
* Does a ping test
* Whole thing is looped for easy batching

## Requirements
* Windows only
* Serial connection to 3702
* Ethernet connection to 3702
* A template configuration file
    * Replace BVI interface ip address with {ip} in config file
    * Replace hostname with {hostname} in config file
    * Put this in the same directory as ac_run.exe
* Firmware file if upgrading (See TODO)

## Usage
1. Use ac_run.exe in /dist/
2. A wizard will launch on first run (not Gandalf unfortunatly)
    * Follow prompts
3. Rest should be self explanitory

## Optional
* A /lists/master.csv (generated on first run)
    * list of devices name,ip
    * Saves manually trying to find an IP address

## Over-simplified algorithm explanation
1. Starts tftp server in a parallel process
2. Checks for a settings.txt file
    * Lauches wizard if it doesn't exist
3. Parameters are stored in a settings.txt file
    * COM port
    * Temp IP address for 3702
    * PC IP address
    * Hostname prefix and suffix
    * Template file location
    * Upper or lowercase for hostname
4. Prompts for a name
5. Looks up name against master.csv to retrieve IP address
    * Prompts if there is no match
6. Generates a config file based on template
7. Initialized serial COM port
8. Waits for 3702 to boot
9. Checks if autonomous
10. Checks firmware version
11. Checks configuration status
12. Does whatever needs to be done at this point
    1. Converts to autonomous if it isn't already
    2. Uploads firmware if it isn't updated
    3. Sets BVI interface with temp IP
    4. Uploads config
    5. Copies config to running-config
13. Performs a ping test and checks if config actually loaded
14. Writes to memory
15. Starts again

## TODO
See TODO