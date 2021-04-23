from BunnyBanners import BunnyBanners
from BunnyConfig import BunnyConfig
from BunnyValidator import BunnyValidator
from termcolor import colored


class BunnyValues:

    @staticmethod
    def GetIPAddress(requestMsg, currentValue):
        while True:
            temp_ip = input(colored(requestMsg, "yellow"))
            if BunnyValidator.IsValidIP(temp_ip):
                return temp_ip
            elif temp_ip == "c" or temp_ip == "C":
                print(colored("Cancelled!", "green"))
                return currentValue

    @staticmethod
    def GetPortNumber(requestMsg, currentValue):
        while True:
            temp_port = input(colored(requestMsg, "yellow"))
            if BunnyValidator.IsValidPortNumber(temp_port):
                return int(temp_port)
            elif temp_port == "c" or temp_port == "C":
                print(colored("Cancelled!", "green"))
                return currentValue

    @staticmethod
    def GetEipOffset(requestMsg, currentValue):
        while True:
            temp_offset = input(colored(requestMsg, "yellow"))
            if BunnyValidator.IsValidEipOffset(temp_offset):
                return int(temp_offset)
            elif temp_offset == "c" or temp_offset == "C":
                print(colored("Cancelled!", "green"))
                return currentValue

    @staticmethod
    def GetShellcode(requestMsg, currentValue):
        while True:
            temp_shellcode = input(colored(requestMsg, "yellow"))
            if BunnyValidator.IsValidShellcode(temp_shellcode):
                return bytes(temp_shellcode, "utf-8")
            elif temp_shellcode == "c" or temp_shellcode == "C":
                print(colored("Cancelled!", "green"))
                return currentValue

    @staticmethod
    def GetBadChars(requestMsg, currentValue):
        while True:
            temp_badchars = input(colored(requestMsg, "yellow"))
            if BunnyValidator.IsValidBadChars(temp_badchars):
                return temp_badchars
            elif temp_badchars == "c" or temp_badchars == "C":
                print(colored("Cancelled!", "green"))
                return currentValue

    @staticmethod
    def GetAddress(requestMsg, currentValue):
        while True:
            temp_address = input(colored(requestMsg, "yellow"))
            if BunnyValidator.IsValidAddress(temp_address):
                return bytes(temp_address, "utf-8")
            elif temp_address == "c" or temp_address == "C":
                print(colored("Cancelled!", "green"))
                return currentValue

    @staticmethod
    def GetOperation(requestMsg, currentValue):
        return bytes(input(colored(requestMsg, "yellow")), "utf-8")


    @staticmethod
    def ManuallySetValue(opNumber):
        if opNumber == '1':
            BunnyConfig.remote_ip = BunnyValues.GetIPAddress("Remote IP: ", BunnyConfig.remote_ip)
        elif opNumber == '2':
            BunnyConfig.remote_port = BunnyValues.GetPortNumber("Remote Port: ", BunnyConfig.remote_port)
        elif opNumber == '3':
            BunnyConfig.local_ip = BunnyValues.GetIPAddress("Local IP: ", BunnyConfig.local_ip)
        elif opNumber == '4':
            BunnyConfig.local_port = BunnyValues.GetPortNumber("Local Port: ", BunnyConfig.local_port)
        elif opNumber == '5':
            BunnyConfig.operation = BunnyValues.GetOperation("Operation: ", BunnyConfig.operation)
        elif opNumber == '6':
            BunnyConfig.eip_offset = BunnyValues.GetEipOffset("EIP Offset: ", BunnyConfig.eip_offset)
        elif opNumber == '7':
            BunnyConfig.address = BunnyValues.GetAddress("Address: ", BunnyConfig.address)
        elif opNumber == '8':
            BunnyConfig.badChars = BunnyValues.GetBadChars("Bad Chars ", BunnyConfig.badChars)
        elif opNumber == '9':
            BunnyConfig.shellcode = BunnyValues.GetShellcode("Shellcode: ", BunnyConfig.shellcode)

    @staticmethod
    def PrintCurrentValues():
        BunnyBanners.PrintCurrentConfigBanner()
        print(colored("\n\n\tRemote IP: " + BunnyConfig.remote_ip +
                      "\n\n\tLocal IP: " + BunnyConfig.local_ip +
                      "\n\n\tRemote Port: " + str(BunnyConfig.remote_port) +
                      "\n\n\tLocal Port: " + str(BunnyConfig.local_port) +
                      "\n\n\tOp: " + BunnyConfig.operation.decode('utf-8') +
                      "\n\n\tOffset: " + str(BunnyConfig.eip_offset) +
                      "\n\n\tAddress: " + BunnyConfig.address.decode('utf-8') +
                      "\n\n\tShellcode: " + BunnyConfig.shellcode.decode('utf-8') +
                      "\n\n\tBad Chars: " + BunnyConfig.badChars + "\n\n", 'cyan'))

        input(colored("\tPress enter to return...", "yellow"))