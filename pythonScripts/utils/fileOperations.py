import os
import time
commandList=["fileOps --findRep", "fileOps --rename", "fileOps --delete"]
def commands(comm):
    print("##### COMMANDS #####")
    print("______________________")
    print(comm)
commands(commandList)
print("______________________")
def fileOps():
    commandEntered=input("Enter a command")