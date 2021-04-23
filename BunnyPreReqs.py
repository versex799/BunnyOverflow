import os
from termcolor import colored


class BunnyPreReqs:
    @staticmethod
    def CheckForPreReqs():
        missingPreReqs = False

        if not os.path.isfile("/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb"):
            missingPreReqs = True
            print(colored("Missing Pre-Req: /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb", "red"))
            exit(0)

        if not os.path.isfile("/usr/share/metasploit-framework/tools/exploit/pattern_create.rb"):
            missingPreReqs = True
            print(colored("Missing Pre-Req: /usr/share/metasploit-framework/tools/exploit/pattern_create.rb", "red"))
            exit(0)

        if not os.path.isfile("/usr/bin/msfvenom"):
            missingPreReqs = True
            print(colored("Missing Pre-Req: /usr/bin/msfvenom", "red"))
            exit(0)