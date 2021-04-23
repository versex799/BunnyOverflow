import os, subprocess
import sys

from termcolor import colored

from BunnyConfig import BunnyConfig


class BunnyEars:
    @staticmethod
    def StartNetCatListener():
        print(colored("\n\nOpening a new terminal window and starting netcat listener...\n\n", "green"))
        nc = "nc -nvlp " + str(BunnyConfig.local_port)

        subprocess.Popen(["qterminal", "-e", nc])