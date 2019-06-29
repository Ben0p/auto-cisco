# Auto Cisco TODO

## Bugs
- [ ] Wigs out if tftp fails

- [x] Names with a hypen won't match (splits string at hypens)
    - Now matches full hostname rather than combining prefix and suffix
- [ ] If settings file is blank it loops forever
- [x] not finding template
    - Was only looking in config/ folder (config/config/template)
- [x] not finding config file
    - Was only looking in config/ folder (config/config/template)
- [ ] ping test a bit wonky
- [ ] If there are alot of configs, template scan will return all
    - [ ] Use template folder or current directory instead
- [ ] WGB temp IP hard coded to be set as 10.0.0.2
    - [ ] Prompt in wizard or generate based on PC ip
    - [ ] Retreive when setting interface on wgb
- [ ] If not configured, only checks for -command hostname and fails
    - [ ] Change to match any hostname other than default (ap>, ap#, ap{mac})


## General
- [ ] Check if PC ip matches what is saved in config
- [ ] Option to reboot wgb to double check or if tests fail
- [ ] Incorporate uppercase or lowercase when writing hostname and files
    - [x] prompt in wizard
    - [x] Record in settings
    - [ ] Apply in config
- [x] Verify all required settings are there
- [ ] Options at statup for task
    - [ ] wipe flash
    - [ ] upload new config
    - [ ] Program new WGB
    - [ ] Change IP and hostname only
    - [ ] Update firmware
- [ ] Scan for firmware image and prompt
- [ ] Generally generalize for any site
- [x] No longer need fleet config
- [x] File in (.csv) with hostname and IP
- [ ] Append configured details to .csv
    - [ ] MAC
    - [ ] Serial
    - [ ] Hostname
    - [ ] Config file name
    - [ ] Completed status
    - [ ] Completed date / time
    - [ ] Checks (ping)
    - [ ] firmware version
- [x] Prompt to overwrite config if 3702 is already configured
- [ ] Check laptop IP
    - [x] Get IP addresses and hostname
    - [ ] Set WGB temp IP to suit or
    - [ ] Prompt to change laptop IP
- [ ] Generate template from an existing config
    - [ ] Replace IP and Hostname with {ip} {hostname}

## Curses
- [ ] Use curses or perhaps a GUI
- [ ] Checklist of completed tasks [OK]

## Config Generator 
- [x] Input info needed
    - [x] List of names needed
    - [x] IP
    - [x] Machine name
    - [x] Base config
- [x] Parse the needed machines list
- [x] Read fleet file in .csv
- [x] Match the vehicle
- [x] Extract IP and Hostname
- [x] Create folder with hostname
- [x] Read default config
- [x] Write generated config
- [x] Prompt to change com port if it fails

## Config management server
- [ ] Server to manage configs and programing dates / times

## Convert to GUI