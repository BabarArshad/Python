# VARIABLE-LENGTH ARGUMENTS

# *args allows you to pass a variable number of non-keyword arguments to a function.

# let me show you how it can help in the IT network industry. Imagine you are a network administrator and you want to create a function that can take any number of IP addresses as input and print them out.

from ast import With


def print_ip_addresses(*args):
    for ip in args:
        print(ip)   

# Now you can call the function with any number of IP addresses:
print_ip_addresses('192.168.1.1', '192.168.1.2', '192.168.1.3') 

# Challenge in Positionnal Arguments:
def ping_devices(ip1, ip2):
    print(f'Pinging {ip1}...')
    print(f'Pinging {ip2}...')

ping_devices('192.168.1.1', '192.168.1.2') # output: pinging 192.168.1.1...
# pinging 192.168.1.2...

# Can you ping five routers instead? 
# ping_devices(
#     '192.168.1.1',
#     '192.168.1.2',
#     '192.168.1.3',
#     '192.168.1.4',
#     '192.168.1.5'
# )
# Error because the function is only designed for 2 devices, what if a different customer have 20 switches? 
# you keep editing the function forever. 

# Challenge in Default Arguments:
# Maybe you think:
def ping_devices(ip1, ip2=''):
    print(ip1)
    print(ip2)
ping_devices('192.168.1.1') 
# or 
ping_devices('192.168.1.1', '192.168.1.2')

# what if we have 20 switches? 
# Default arguments only make parameters optional.
# They don't make the number of parameters unlimited.

# Challenge in Keyword Arguments:
def ping_devices(source_ip, destination_ip):

    print(source_ip)
    print(destination_ip)

ping_devices(
    source_ip='10.0.0.1',
    destination_ip='8.8.8.8'
)
# Keyword arguments improve readability.
# but again it has same problem as positional and default arguments that impossible to ping 20 switches without editing the function.

# Well We can solve this problem by using *args and **kwargs.

def ping_devices(*devices):

    for device in devices:
        print(f"Pinging {device}...")
ping_devices(
    '192.168.1.1',
    '192.168.1.2'
) # output: pinging 192.168.1.1...
# pinging 192.168.1.2...

# tomorrow 
ping_devices(
    '192.168.1.1',
    '192.168.1.2',
    '192.168.1.3',
    '192.168.1.4',
    '192.168.1.5'
) # output: pinging 192.168.1.1...
# pinging 192.168.1.2...
# pinging 192.168.1.3...
# pinging 192.168.1.4...
# pinging 192.168.1.5...    


# next week 100 devices ? no problem, just add them to the function call.

print('------------------------KWARGS------------------------')
# **KWARGS 

# Imagine you don't know how many VLANS you want to configure and you use *args Like: 
def configure_vlans(*args):
    print(args)

# Call the function with any number of VLANs:
configure_vlans(10,20,30,40) # output: (10, 20, 30, 40)
# Notice 
# args is a tuple.

# the question is What if the number of keyword arguments is unknown?
# Imagine we write a script and sometimes we configure:
#   hostname, ip, mask, gateway, dns, snmp, ntp, location, contact
#
# Sometimes only:
#   hostname, ip
#
# Sometimes:
#   hostname, ip, dns
#
# Without **kwargs, you'd have to do this:
#   def configure_device(
#       hostname=None,
#       ip=None,
#       gateway=None,
#       dns=None,
#       ntp=None,
#       snmp=None,
#       contact=None,
#       location=None,
#       vlan=None,
#       ...
#   ):
# That becomes ugly.
#
# With **kwargs, you can do this:

def configure_device(**kwargs):
    print(kwargs)
# Now Call
configure_device(
    hostname='SW1',
    ip='192.168.1.10',
    dns='8.8.8.8',
    location='Datacenter'
)

# output: {
#  'hostname': 'SW1',
#  'ip': '192.168.1.10',
#  'dns': '8.8.8.8',
#  'location': 'Datacenter'
# }

# Notice something.

# kwargs is NOT a tuple.

# It is a dictionary.

# {
#  key : value
# }


# Why can't we use *args instead?
# Imagine
# configure_device(
#     "SW1",
#     "192.168.1.10",
#     "255.255.255.0",
#     "8.8.8.8"
# )
# # can you tell which value is DNS, subnet mask, IP address, or hostname?
# # With **kwargs, you can specify the key for each value, making it clear what each value represents.

# configure_device(
#     hostname="SW1",
#     ip="192.168.1.10",
#     mask="255.255.255.0",
#     dns="8.8.8.8"
# )


# Real-world Network Engineer Example
def create_switch(**kwargs):

    for command, value in kwargs.items():
        print(f"{command} {value}")

# Call the function with any number of configuration commands:
create_switch(
    hostname="CORE1",
    domain="company.local",
    ntp="192.168.100.5",
    snmp="public",
    vlan=100
)
# You didn't need to define
# hostname
# domain
# ntp
# snmp
# vlan
# inside the function.
# It accepts whatever keyword arguments you pass.