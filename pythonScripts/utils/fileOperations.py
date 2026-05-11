import os
import time
commandList=["fileOps--findRep", "fileOps--rename", "fileOps--delete", "fileOps--quit"]
userProfile=os.environ["USERPROFILE"]
def fileOps():
 def commands(comm):
    print("##### COMMANDS #####")
    print("______________________")
    print(comm)
 commands(commandList)
 print("______________________")
 while True:
    commandEntered = input("Enter a command.\n").strip()
    print("______________________")
    if commandEntered in commandList:
        if commandEntered == commandList[0]:
            filePath = input("Enter the file path.\n").strip()
            print("______________________")
            if filePath.startswith("C:") or filePath.startswith("c:"):
                with open(filePath, "r", encoding='utf-8') as f:
                    file = f.read()
                find = input("Enter what to find.\n").strip()
                if find in file:
                    repl = input("Enter what to replace it with.\n").strip()
                    newFile = file.replace(find, repl)
                    with open(filePath, "w", encoding='utf-8') as f:
                        f.write(newFile)
                else:
                    print("### No results ###")
            else:
                print("### INVALID PATH ###")
        elif commandEntered == commandList[1]:
            filePathRename = input("Enter the file path to rename.\n").strip()
            print("______________________")
            newPath = input("Enter the new path.\n")
            if filePathRename.startswith("C:") or filePathRename.startswith("c:"):
                print("______________________")
                os.rename(filePathRename, newPath)
            else:
                print("### INVALID PATH ###")
        elif commandEntered == commandList[2]:
            filePathDel = input("Enter the file path to be deleted.\n").strip()
            if filePathDel.startswith("C:") or filePathDel.startswith("c:"):
                os.remove(filePathDel)
            else:
                print("### INVALID PATH ###")
        elif commandEntered == commandList[3]:
            progBarQuit = ""
            for i in range(20):
                progBarQuit += "#"
                print(f"[{progBarQuit}] [Quitting file operations..]", end="\r", flush=True)
                time.sleep(0.1)
            print()
            return
    else:
        print("Invalid command!")


fileOps()