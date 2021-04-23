import os

from BunnyValidator import BunnyValidator


class BunnyCommon:

    @staticmethod
    def ClearScreen():
        if "nt" in os.name:
            _ = os.system("cls")
        else:
            _ = os.system("clear")

    @staticmethod
    def ConvertAddress(address):
        if BunnyValidator.IsValidAddress(address):
            return "\\x" + address[6:8] + "\\x" + address[4:6] + "\\x" + address[2:4] + "\\x" + address[0:2]
        else:
            return ""
