# BunnyOverflow

![BunnyOverflow](https://github.com/versex799/BunnyOverflow/blob/master/Screenshots/BunnyOverFlowBanner.png)

The goal was to create an application that helped to speed up the process of creating simple Windows-based buffer overflow exploits by automated certain parts of it. 

When you run BunnyOverflow you will be greeted by a main menu that allows you to either run each one of the processes independently or in the form of a simple walkthrough.
At the end you will have the ability to save your buffer overflow configuration for use at a later date. As each process completes, the results of that process will be 
automatically saved in an autosave file which will be detected at the next run and can be imported to prevent you from having to manually enter the same information over
and over again.

You can see a video demonstration of BunnyOverflow on my youtube channel using the link below.

https://www.youtube.com/watch?v=QOR5xybnf7Y

# Configurations

![Configuration Auto Load](https://github.com/versex799/BunnyOverflow/blob/master/Screenshots/AutoLoadConfig.png)

When the script runs it will check for a bof.autosave file. This file will contain any information that will be used between the processes or that will be needed
between script executions. Any time you run one of the processes or you manually change a configuration value, it will be saved to this file. If an error were to
occur or you needed to exit the script for some reason, you will be prompted on the next execution to load the configuration. If you choose not to load this
configuration, you will need to manually re-enter the information and/or run through the processes again.

# Configuration Settings

  1: Remote IP - IP address of the target box
  
  2: Remote Port - Port that the vulnerable service is running on
  
  3: Local IP - The IP address used for connecting back via reverse shell
  
  4: Local Port - The port to use for the reverse shell
  
  5: Operation - The operation to perform on the vulnerable service
  
  6: EIP Offset - The offset used for overwriting the EIP
  
  7: Address - The vulnerable address that will be written to the EIP
  
  8: Bad Chars - The Bad Characters that need to be excluded from the shellcode
  
  9: Shellcode - The malicious shellcode for the reverse shell

# Download and Run

To download the script simply enter `git clone https://github.com/versex799/BunnyOverflow.git`

Change directoy `cd BunnyOverflow`

Run the script `python3 BunnyOverflow.py`


# Main Menu

![Main Menu](https://github.com/versex799/BunnyOverflow/blob/master/Screenshots/MainMenu.png)

The main menu allows you to select running any one of the processes, or running them all at once, where one carries directly over to the next. I will go over each
of the options in more detail below. 

# 1: Start New BOF
 
The purpose of this process is to create a walkthrough type of experience. It takes you through each of the following processes and provides prompts to let you know
what to look at, when to reset the debugger, and more. After each step is finished, the results will automatically be saved to disk. If no previous configuration was
detected at startup or was not loaded before beginning this process, the user will be prompted to enter the remote and local IP addresses and port numbers, as well as
the operation to perform on the service. 

# 2: Fuzzing

Fuzzing is the process of determining if and when a service crashes based on the input values supplied to it. This simple operation makes multiple connections to the
target and sends a payload to see if the program will crash. Each connection increases the size of the payload delivered to the target. 

# 3: EIP Offset

Once fuzzing is complete it is important to determine exactly how big the payload needs to be in order to overwrite the EIP. This is determined by sending a unique
pattern of characters to the target. When the service crashes, part of that unique pattern of characters will be displayed in the EIP inside the debugger. This small
portion of the pattern is used to determine how far from the beginning of the buffer, the EIP is. This will be used in future processes to inject a vulnerable address.

# 4: Bad Characters

Next, we need to find the bad characters. These are characters that we will need to avoid putting in the malicious shellcode. Each vulnerable service will have different
characters that will cause problems if they are included in the shellcode. In this operation, we send another special sequence of characters to the target. Once the
target service has crashed we can look in the debugger to see which characters are out of place or missing. 

*** NOTE *** It may be helpful to utilize the "Find BadChars" program to help complete this process. You can find it here https://github.com/versex799/Find_BadChars.

# 5: Generate Shellcode

After the bad characters have been detected, we can generate a payload based on the target machine. To keep this script simple, it will generate either an x86 or x64
based reverse shell using msfvenom. As of right now, there is no option for meterpeter. If that is something someone would like to add, then feel free.

# 6: Vulnerable Address

This process is relatively straight-forward, and is one of the most manual processes in the script. Here, you will need to find a vulnerable address that can be used
to inject our malicious payload. The instructions for how to do that will be displayed to make it easier. 

# 7: Exploit

Now it is time to actually exploit the target. All this process does, is take the results from the previous processes, puts them together and sends the final payload to
the target. A netcat listener will be started automatically before the payload is sent.

# 8: Change Config

This simply allows you to manually edit individual configuration settings.

# 9: View Current Config

Shows what each configuration is currently set to.

# A: Load

Allows you to load a configuration for a previous buffer overflow.

# B: Save

Allows you to save the current buffer overflow configuration under a different filename. This may come in handy if you are working on different buffer overflows
or if you simply wish to keep the configurations for the buffer overflows you have completed already.

# C: Exit

Self-explanatory. 
