# Auto Cisco TODO

## General
- [ ] No longer need fleet config
- [ ] File in (.csv) with hostname and IP
- [ ] Folders for each device
    - [ ] details .csv
    - [ ] details .json
    - [ ] auto-config-log.txt
    - [ ] command config
    - [ ] fleet config
- [ ] File out (.csv) with details (all)
- [ ] File out (.json) with details (all - for future database parsing)
- [ ] Details for files
    - [ ] MAC
    - [ ] Serial
    - [ ] Hostname
    - [ ] Fleet config file name
    - [ ] Command config file name
    - [ ] Completed status
    - [ ] Completed date / time
    - [ ] Checks (ping)
    - [ ] firmware version
- [ ] Prompt to overwrite config if 3702 is already configured
  


## Config Generator 
- [ ] Input info needed
    - [ ] List of names needed
    - [ ] Fleet IP (TropOS 5ghz)
    - [ ] Command IP
    - [ ] Machine name
    - [ ] Fleet base config
    - [ ] Command base config
- [ ] Ouput files needed
    - [ ] Master list?
    - [ ] Completed configs status
        - [ ] Name, failed/OK/skipped ...
    - [ ] Folder for each machine
        - [ ] fleet config
        - [ ] command config
- [ ] Parse the needed machines list
- [ ] Read fleet file in .csv
- [ ] Match the
- [ ] Extract IP and Hostname
- [ ] Create folder with hostname
- [ ] Read default fleet config
- [ ] Write generated fleet config
- [ ] Read default command config
- [ ] Write generated command config
- [ ] Prompt to change com port if it fails

## Config management server
- [ ] Server to manage configs and programing dates / times