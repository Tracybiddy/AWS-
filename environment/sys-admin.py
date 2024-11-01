#Using os.system
import os
os.system("ls")

#Using subprocess.run
import subprocess
subprocess.run(["ls"])

#Long listing
subprocess.run(["ls","-l"])

#Listing with a specified file name
subprocess.run(["ls","-l","README.md"])

#Retrieving system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Retrieving information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])
