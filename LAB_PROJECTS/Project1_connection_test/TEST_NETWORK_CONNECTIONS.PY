# PROJECT: TEST NETWORK CONNECTIONS

# import subprocess
# commands = 'ping -c 4 8.8.8.8' # for Linux and Mac
# # command = 'ping -n 4 google.com' # for Windows

# output = subprocess.check_output(commands.split())
# print(output.decode())

# The above code runs a shell command and saves the output in a variable called output which is then dislayed at the terminal. 
# as of now the focus is on exception handling.
# existing pythong module "subprocess" is imported. 
# declaring a string variable for the command to be executed.
# Called the check_output function from the module
# The function expects the command argument as a list instead of a string,
# so the command is split using the split() method
# Finally, the output is printed after decoding it as a UTF-8 string

## if we change the IP, this exception will be raised: subprocess.CalledProcessError: Command '['ping', '-c', '4', '8.8.8.3']' returned non-zero exit status 1.

# Now lets change the script the script to ping all the IPs in hosts.txt file and handle the exception if any of the IPs are not reachable.
'''
8.8.8.8
6.77.7.8
8.8.4.4
1.1.1.1
'''
# If any hosts is not responding, the script should display the message host down and move to the next host in the list and ping it.

# first we will read the hosts.txt file and store the IPs in a list
import subprocess


with open('hosts.txt') as file:
    ip_addresses = file.read().splitlines() # read the file and split the lines into a list
    # print(ip_addresses) # comment the above code and am printing just to see if the IPs are being read correctly
# ['8.8.8.8', '6.77.7.8', '8.8.4.4', '1.1.1.1'] reading file correctly
# now lets run the code for each IP in the list. moving the code insie a for loop 
    # for ip in ip_addresses:
    #     commands = f'ping -c 1 {ip}'
    #     output = subprocess.check_output(commands.split())
    #     print(output.decode())

# the 2nd IP address is not responding giving the error: subprocess.CalledProcessError: Command '['ping', '-c', '4', '6.77.7.8']' returned non-zero exit status 2.
# Lets remove that IP and run the script again. and each IP is responding correctly.

# Lets put the non responding IP back and handle the exception using try and except block.

    for ip in ip_addresses:
        try:
            commands = f'ping -c 1 {ip}'
            output = subprocess.check_output(commands.split())
            print(output.decode())
        except Exception as e:
            print(f'Host {ip} is down => {e}')  
# the above code will catch any exception that occurs while trying to ping the host and print a message indicating that the host is down along with the error message.
        print ('#' * 50) # just to separate the output of the script from the next one.



