from BunnyBanners import BunnyBanners
from BunnyCommon import BunnyCommon
from BunnyFuzz import BunnyFuzz
from BunnyOffset import BunnyOffset
from BunnyPayload import BunnyPayload
from BunnyValues import BunnyValues
from BunnyRun import BunnyRun
from BadBunnyChars import BadBunnyChars
from BunnyAddress import BunnyAddress
from termcolor import colored
from BunnyConfig import BunnyConfig


class BunnyMenu:
    config = None

    @staticmethod
    def GetUserSelection():

        userSelection = BunnyMenu.PrintMenu()
        operationResult = BunnyMenu.PerformSelectedOperation(userSelection)

        while True:
            if operationResult == 'valid':
                userSelection = BunnyMenu.PrintMenu()
            elif operationResult == 'invalid':
                userSelection = input("Selection: ")

            operationResult = BunnyMenu.PerformSelectedOperation(userSelection)

    @staticmethod
    def PerformSelectedOperation(userSelection):
        if userSelection != '7':
            BunnyMenu.GetInitialBofInformation()

        if userSelection == '1':
            if not BunnyFuzz.Fuzz():
                return "valid"
            BunnyMenu.config.SaveCustomConfig(True)

            if not BunnyOffset.FindEIPOffset():
                return "valid"
            BunnyMenu.config.SaveCustomConfig(True)

            if not BadBunnyChars.FindBadChars():
                return "valid"
            BunnyMenu.config.SaveCustomConfig(True)

            if not BunnyPayload.GeneratePayload():
                return "valid"
            BunnyMenu.config.SaveCustomConfig(True)

            if not BunnyAddress.FindVulnAddress():
                return "valid"
            BunnyMenu.config.SaveCustomConfig(True)

            BunnyRun.Exploit()
            return "valid"
        if userSelection == '2':
            BunnyFuzz.Fuzz()
            return "valid"
        elif userSelection == '3':
            BunnyOffset.FindEIPOffset()
            return "valid"
        elif userSelection == '4':
            BadBunnyChars.FindBadChars()
            return "valid"
        elif userSelection == '5':
            BunnyPayload.GeneratePayload()
            return "valid"
        elif userSelection == '6':
            BunnyAddress.FindVulnAddress()
            return "valid"
        elif userSelection == '7':
            BunnyRun.Exploit()
            return "valid"
        elif userSelection == '8':
            opNumber = BunnyMenu.PrintSetValuesMenu()
            BunnyValues.ManuallySetValue(opNumber)
            BunnyMenu.config.SaveCustomConfig(True)
            return "valid"
        elif userSelection == '9':
            BunnyValues.PrintCurrentValues()
            return "valid"
        elif userSelection == 'A' or userSelection == 'a':
            BunnyMenu.config.LoadConfig(False)
            return "valid"
        elif userSelection == 'B' or userSelection == 'b':
            BunnyMenu.config.SaveCustomConfig(False)
            return "valid"
        elif userSelection == 'C' or userSelection == 'c':
            exit()
        elif userSelection == 'M' or userSelection == 'm':
            return "menu"

        else:
            print("Invalid selection. Please choose an option from the menu using the digits 1 - 9 or type M to see "
                  "the menu options again\n")
            return "invalid"

    @staticmethod
    def PrintMenu():
        BunnyBanners.PrintMainBanner()
        print(colored(
            "\n\nPlease select the operation you would like to perform. You can either start a new Buffer Overflow\n"
            "which will run through all the operations, or perform any of the operations individually. You may also\n"
            "load an existing buffer overflow that you have saved previously.\n",
            "green"))
        print(colored(
            "\n\n\t1: Start New BOF\t- Walk through operations 2 - 7"
            "\n\n\t2: Fuzzing\t\t- Attempt to crash a vulnerable service by sending payloads increasing in size"
            "\n\n\t3: EIP Offset\t\t- Find the offset number that allows you to overwrite the EIP"
            "\n\n\t4: Bad Characters\t- Find out what characters cannot be used in the payload"
            "\n\n\t5: Generate Shellcode\t- Generate a payload used to create reverse shell"
            "\n\n\t6: Vulnerable Address\t- Find an address where our payload can be injected"
            "\n\n\t7: Exploit\t\t- Send the result of all previous operations to the target to gain a reverse shell"
            "\n\n\t8: Change Config\t- Manually set values for configured variables"
            "\n\n\t9: View Current Config\t- See what the current configuration looks like"
            "\n\n\tA: Load\t\t\t- Load a previously saved config for a buffer overflow"
            "\n\n\tB: Save\t\t\t- Save your current config to disk with a custom filename"
            "\n\n\tC: Exit", "cyan"))
        return input(colored("\n\tSelection: ", "yellow"))


    @staticmethod
    def PrintSetValuesMenu():
        BunnyBanners.PrintChangeConfigBanner()
        print(colored(
            "\n\t1: Set Remote IP"
            "\n\t2: Set Remote Port"
            "\n\t3: Set Local IP"
            "\n\t4: Set Local Port"
            "\n\t5: Set Operation"
            "\n\t6: Set EIP Offset"
            "\n\t7: Set Address"
            "\n\t8: Set Bad Chars"
            "\n\t9: Set Shellcode"
            "\n\n\tEnter: Return to Main Menu", "cyan"))
        return input(colored("\n\tSelection: ", "yellow"))

    @staticmethod
    def GetInitialBofInformation():
        # Get the Remote IP
        if not BunnyConfig.remote_ip or BunnyConfig.remote_ip == "":
            BunnyConfig.remote_ip = BunnyValues.GetIPAddress("Enter Target IP: ", "")

        # Get the Remote Port
        if not BunnyConfig.remote_port or BunnyConfig.remote_port == "":
            BunnyConfig.remote_port = BunnyValues.GetPortNumber("Enter Target Port: ", 0)

        # Get the Local IP
        if not BunnyConfig.local_ip or BunnyConfig.local_ip == "":
            BunnyConfig.local_ip = BunnyValues.GetIPAddress("Enter Local IP: ", "")

        # Get the Local Port
        if not BunnyConfig.local_port or BunnyConfig.local_port == "":
            BunnyConfig.local_port = BunnyValues.GetPortNumber("Enter Local Port: ", 0)

        # Get the operation performed on the remote service
        if not BunnyConfig.operation or BunnyConfig.operation == "":
            BunnyConfig.operation = BunnyValues.GetOperation("Enter Operation: ", b"")

        BunnyMenu.config.SaveCustomConfig(True)
