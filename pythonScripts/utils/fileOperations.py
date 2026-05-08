import os
commandList=["fileOps --findRep", "fileOps --rename", "fileOps --delete", "fileOps --quit"]

def fileOps():
    def commands(comm):
     print("##### COMMANDS #####")
     print("______________________")
     print(comm)
    commands(commandList)
    print("______________________")
    commandEntered=input("Enter a command.")
    print("______________________")
    if commandEntered in commandList:
        if commandEntered==commandList[0]:
            filePath=input("Enter the file path.")
            print("______________________")
            if filePath.startswith("C:") or filePath.startswith("c:"):
                with open(filePath, "r", encoding='utf-8') as f:
                    file=f.read()
                find=input("Enter what to find.")
                if find in file:
                    repl=input("Enter what to replace it with.")
                    newFile=file.replace(find, repl)
                    with open(filePath, "w", encoding='utf-8') as f:
                     file=f.write(newFile)
                else:
                    print("### No results ###")
            else:
                print("### INVALID PATH ###")
        elif commandEntered==commandList[1]:
            filePathRename=input("Enter the file path to rename.")
            print("______________________")
            newName=input("Enter the new name.")
            print("______________________") if filePathRename.startswith("C:") or filePathRename.startswith("c:") else print("### INVALID PATH ###")
            os.rename(filePathRename, newName)
        elif commandEntered==commandList[2]:
            filePathDel=input("Enter the file path to be deleted.")
            os.remove(filePathDel) if filePathDel.startswith("C:") or filePathDel.startswith("c:") else print("### INVALID PATH ###")
        elif commandEntered==commandList[3]:
            return
    else:
        print("Invalid command!")