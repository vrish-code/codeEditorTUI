import os
import time
commandList=["fileOps--findRep", "fileOps--rename", "fileOps--delete", "fileOps--quit", "fileOps--help", "fileOps--info"]
userProfile=os.environ["USERPROFILE"]
info = """This core text editor module automates terminal-driven file system actions on Windows.
It grants direct local access to search and replace text, rename files, and delete items."""

help = f"""
======================================================================
                        📋 OPERATION COMMANDS
======================================================================
  🔹 fileOps--findRep : Search file content and replace matching strings.
  🔹 fileOps--rename  : Move or change a file path to a new location.
  🔹 fileOps--delete  : Instantly remove a target file from disk.
  🔹 fileOps--quit    : Safely terminate the file operations sub-shell.

⚠️ REQUIREMENT RULES:
  • Paths must target your main storage drive partition (C: or c:).
  • All file deletion commands bypass the Windows Recycle Bin.
  • Active Workspace User Profile: {userProfile}
======================================================================
"""
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
        elif commandEntered == commandList[4]:
            print(info)
        elif commandEntered ==commandList[5]:
            print(help)
    else:
        print("### INVALID COMMAND ###")

