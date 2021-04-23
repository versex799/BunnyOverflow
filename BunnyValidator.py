import re
from termcolor import colored


class BunnyValidator:
    def __init__(self):
        pass

    @staticmethod
    def IsValidIP(ipAddr):
        ipMatch = re.match(r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', ipAddr)

        if not ipMatch and ipAddr:
            print(colored("Invalid IP address\n\n", "red"))
            return False
        else:
            return True

    @staticmethod
    def IsValidPortNumber(portNumber):
        portMatch = re.match(r'[0-9]{1,5}', portNumber)

        if not portMatch and portNumber:
            print(colored("Invalid port number\n\n", "red"))
            return False
        else:
            return True

    @staticmethod
    def IsValidAddress(address):
        addrMatch1 = re.match(r'[a-zA-Z0-9]{8}', address)

        if not addrMatch1 and address:
            addrMatch2 = re.match(r'(\\x[a-zA-Z0-9]{2}){4}', address)
            if not addrMatch2:
                print(colored("Invalid address\n\n", "red"))
                return False
            else:

                return True
        else:
            return True

    @staticmethod
    def IsValidEipOffset(offset):
        offsetMatch = re.match(r'[0-9]{1,6}', offset)

        if not offsetMatch and offset:
            print(colored("Invalid EIP Offset\n\n", "red"))
            return False
        else:
            return True

    @staticmethod
    def IsValidShellcode(shellcode):
        shellcodeMatch = re.match(r'(\\x[a-zA-Z0-9]{2})+', shellcode)

        if not shellcodeMatch and shellcode:
            print(colored("Invalid Shellcode\n\n", "red"))
            return False
        else:
            return True

    @staticmethod
    def IsValidBadChars(badchars):
        badcharsMatch = re.match(r'(\\x[a-zA-Z0-9]{2} ?)+', badchars)

        if not badcharsMatch and badchars:
            print(colored("Invalid Bad Characters\n\n", "red"))
            return False
        else:
            return True