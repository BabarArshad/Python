
# A namespace is simply a place where Python stores variable names and what they refer to.
# 
# for example, see below example of company network. 
# Head Office
# │
# ├── VLAN 10
# │      Printer
# │      Laptop
# │      Server
# │
# ├── VLAN 20
# │      Printer
# │      Laptop
# │
# └── VLAN 30
#        Printer
# Notice every VLAN can have a device called "Printer". There is no conflict because each VLAN has its own "space."


# Example
hostname = "CORE1"

def configure():

    hostname = "ACCESS1"

    print(hostname)

configure()

print(hostname)
# output: there are two different namespaces. 
# ACCESS1 - Function namespace.
# CORE1 - Global namespacce. 

print("-------------------SCOPE--------------------------------")

# SCOPE 
# A scope is where Python is allowed to look for them.

hostname2 = "CORE2"

def configure():

    print(hostname2)

configure()

# output:
# CORE2 - Global namespace. Inside the function, Python couldn't find hostname locally.

# The LEGB Rule
# Local, Enclosing, Global, Built-in

# Local: 
def configure():

    hostname3 = "SW1"

    print(hostname3)

configure()

# output:
# SW1 - Local namespace. Python first finds local variable, in this case it finds hostname3.

# Enclosing: 
# Suppose a function is inside another function.
def outer():

    hostname4 = "CORE1"

    def inner():

        print(hostname4)

    inner()

outer()

# output:
# CORE1 - Enclosing namespace. Python first looks for local variable, then enclosing variable,
# in this case it finds hostname4.

# Global:
hostname5 = "CORE1"

def configure():

    print(hostname5)

configure()

# output:
# CORE1 - Global namespace. Python couldn't find hostname5 locally, so it looks in the global namespace.

# Built-in:
# Python has a built-in namespace that contains functions and exceptions that are always available.
# for example: 
# print()
# len()
# max()
# min()

# when python can't find a variable in the local, enclosing, or global namespaces, it looks in the built-in namespace.


