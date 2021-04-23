import os
from BunnyValidator import BunnyValidator
from BunnyBanners import BunnyBanners
from termcolor import colored


class BunnyConfig:
    remote_ip = ""
    local_ip = ""
    local_port = 0
    remote_port = 0
    operation = b""
    badChars = ""
    eip_offset = 0
    address = b""
    shellcode = b""
    socketTimeout = 5
    crashCount = 0
    savedConfigLoaded = False

    def __init__(self):
        self.temp_remote_ip = ""
        self.temp_local_ip = ""
        self.temp_local_port = 0
        self.temp_remote_port = 0
        self.temp_operation = b""
        self.temp_badChars = ""
        self.temp_eip_offset = 0
        self.temp_address = b""
        self.temp_shellcode = b""



    def ReinitializeTempVariables(self):
        self.temp_remote_ip = ""
        self.temp_local_ip = ""
        self.temp_local_port = 0
        self.temp_remote_port = 0
        self.temp_operation = b""
        self.temp_badChars = ""
        self.temp_eip_offset = 0
        self.temp_address = b""
        self.temp_shellcode = b""


    def LoadConfig(self, loadDefaultConfig):

        if not loadDefaultConfig:
            BunnyBanners.PrintLoadBanner()
            configPath = input(colored("Path to saved BOF config file (type c to cancel): ", "yellow"))

            if configPath == 'c' or configPath == 'C':
                return
        else:
            configPath = "bof.autosave"

        if os.path.isfile(configPath):
            self.ReinitializeTempVariables()

            if not loadDefaultConfig:
                confirm = input(colored("\n\nThis operation will overwrite all existing values. Do you wish to continue (Y/n)? ", "yellow"))

                if confirm != 'y' and confirm != 'Y' and confirm != '':
                    print(colored("Cancelling load operation!", "green"))
                    return

            f = open(configPath, "r")

            print(colored("The following configuration has been loaded:\n\n", "green"))

            while True:
                configItem = f.readline()

                if not configItem:
                    break

                print("\t" + colored(self.AssignTempVariable(configItem), "cyan"))

            confirm = input(colored("\n\nWould you like to load this configuration (Y/n)? ", "yellow"))

            if confirm != 'y' and confirm != 'Y' and confirm != '':
                input(colored("\n\nCancelling load operation!\n\n", "green"))
                return
            else:
                if not loadDefaultConfig:
                    input(colored("\n\nConfiguration Loaded!\n\n", "green"))
                self.AssignConfigVariables()
        elif not loadDefaultConfig:
            print("Could not find file: " + configPath)

    def AssignTempVariable(self, configItem):
        splitItem = configItem.split('=')
        if splitItem[0] == 'remote_ip':
            if BunnyValidator.IsValidIP(splitItem[1].replace("\n", "")):
                self.temp_remote_ip = splitItem[1].replace("\n", "")
                return "Remote IP: " + splitItem[1]

        elif splitItem[0] == 'local_ip':
            if BunnyValidator.IsValidIP(splitItem[1].replace("\n", "")):
                self.temp_local_ip = splitItem[1].replace("\n", "")
                return "Local IP: " + splitItem[1]

        elif splitItem[0] == 'bad_chars':
            if BunnyValidator.IsValidBadChars(splitItem[1].replace("\n", "")):
                self.temp_badChars = splitItem[1].replace("\n", "")
                return "Bad Chars: " + splitItem[1]

        elif splitItem[0] == 'remote_port':
            if BunnyValidator.IsValidPortNumber(splitItem[1].replace("\n", "")):
                self.temp_remote_port = int(splitItem[1])
                return "Remote Port: " + splitItem[1]

        elif splitItem[0] == 'local_port':
            if BunnyValidator.IsValidPortNumber(splitItem[1].replace("\n", "")):
                self.temp_local_port = int(splitItem[1])
                return "Local Port: " + splitItem[1]

        elif splitItem[0] == 'operation':
            self.temp_operation = bytes(splitItem[1].replace("\n", ""), 'utf-8')
            return "Operation: " + splitItem[1]

        elif splitItem[0] == 'eip_offset':
            if BunnyValidator.IsValidEipOffset(splitItem[1].replace("\n", "")):
                self.temp_eip_offset = int(splitItem[1])
                return "EIP Offset: " + splitItem[1]

        elif splitItem[0] == 'address':
            if BunnyValidator.IsValidAddress(splitItem[1].replace("\n", "")):
                self.temp_address = bytes(splitItem[1].replace("\n", ""), 'utf-8')
                return "Address: " + splitItem[1]

        elif splitItem[0] == 'shellcode':
            if BunnyValidator.IsValidShellcode(splitItem[1].replace("\n", "")):
                self.temp_shellcode = bytes(splitItem[1].replace("\n", ""), 'utf-8')
                return "Shellcode: " + splitItem[1]

    def AssignConfigVariables(self):
        BunnyConfig.remote_ip = self.temp_remote_ip
        BunnyConfig.local_ip = self.temp_local_ip
        BunnyConfig.local_port = self.temp_local_port
        BunnyConfig.remote_port = self.temp_remote_port
        BunnyConfig.operation = self.temp_operation
        BunnyConfig.badChars = self.temp_badChars
        BunnyConfig.eip_offset = self.temp_eip_offset
        BunnyConfig.address = self.temp_address
        BunnyConfig.shellcode = self.temp_shellcode

        BunnyConfig.savedConfigLoaded = True

    def SaveCustomConfig(self, isAutoSave):
        if not isAutoSave:
            BunnyBanners.PrintSaveBanner()
            print(colored("The following information will be saved\n\n\tRemote IP: " + self.remote_ip +
                          "\n\tLocal IP: " + self.local_ip +
                          "\n\tRemote Port: " + str(self.remote_port) +
                          "\n\tLocal Port: " + str(self.local_port) +
                          "\n\tOp: " + self.operation.decode('utf-8') +
                          "\n\tOffset: " + str(self.eip_offset) +
                          "\n\tAddress: " + self.address.decode('utf-8') +
                          "\n\tShellcode: " + self.shellcode.decode('utf-8') +
                          "\n\tBad Chars: " + self.badChars, 'cyan'))

            confirm = input("Do you wish to continue (Y/n)? ")

            if confirm != 'y' and confirm != 'Y' and confirm != '':
                input(colored("Cancelling load operation!", "green"))
                return

            saveLocation = input("Save location: ")
        else:
            saveLocation = "bof.autosave"

        try:
            wFile = ["remote_ip=" + self.remote_ip + "\n",
                     "local_ip=" + self.local_ip + "\n",
                     "remote_port=" + str(self.remote_port) + "\n",
                     "local_port=" + str(self.local_port) + "\n",
                     "operation=" + self.operation.decode('utf-8') + "\n",
                     "eip_offset=" + str(self.eip_offset) + "\n",
                     "shellcode=" + self.shellcode.decode('utf-8') + "\n",
                     "address=" + self.address.decode('utf-8') + "\n",
                     "bad_chars=" + self.badChars]

            f = open(saveLocation, "w+")
            f.writelines(wFile)
            f.close()
        except:
            input(colored("Error saving config file to: " + saveLocation, "red"))

        if not isAutoSave:
            input(colored("Save Successful! Press enter to go back to the main menu... ", "yellow"))