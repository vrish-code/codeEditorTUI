import os
import time
commandList=["fileOps --findRep", "fileOps --rename", "fileOps --delete", "fileOps --quit"]
def commands(comm):
    print("##### COMMANDS #####")
    print("______________________")
    print(comm)
commands(commandList)
print("______________________")
def fileOps():
    commandEntered=input("Enter a command.")
    if commandEntered in commandList:
        if commandEntered==commandList[0]:
            filePath=input("Enter the file path.")
            if filePath.startswith("C:") or filePath.startswith("c:"):
                with open(filePath, "r", encoding='utf-8') as f:
                    file=f.read()
    else:
        print("Invalid command!")