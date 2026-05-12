import os
import time
info = """This workspace module loads the core CLI code engine for active file manipulation.
It reads raw code streams, generates fresh script paths, and opens direct multi-line text editors."""

help = f"""
======================================================================
                        📝 EDITOR COMMANDS
======================================================================
  🔹 editor--open : Open an existing script file to inspect or edit text.
  🔹 editor--new  : Create a brand new file with automated line indexing.
  🔹 editor--read : Display file contents to the viewport without editing.
  🔹 editor--quit : Exit out of the code editor module interface.

⚠️ RUNTIME WORKFLOW NOTE:
  • Line Termination : Type 'cl' on an empty line to freeze and close edits.
  • Path Verification: Requires absolute storage addresses starting with C:.
  • File Protection  : Target system locks active scripts inside the container.
======================================================================
"""

def codeEditor():
    commandsGlobal=["editor--open", "editor--new", "editor--quit", "editor--read", "editor--help", "editor--info"]
    def commandMode(commands):
        print("___________________________________")
        print("##### COMMANDS #####")
        print(commands,"\n")
        print("_______________________")
    commandMode(commandsGlobal)
    while True:
        commEntered = input("Enter a command\n").strip()
        if commEntered in commandsGlobal:
            if commEntered == "editor--open":
                filePath = input("Enter the file path to be opened.\n").upper().strip()
                print("_______________________________")
                if filePath.startswith("C:"):
                    if os.path.exists(filePath):
                        with open(filePath, "r", encoding='utf-8') as f:
                            codeOpened = f.read()
                        print(codeOpened)
                        print("_______________________________")

                        codeEdit = input("Edit code (press cl to stop editing)? (Y/n)").upper().strip()
                        if codeEdit == "Y":
                            newCode = []
                            while True:
                                codeLn = input()
                                if codeLn == "cl":
                                    break
                                newCode.append(codeLn)
                            if newCode:
                                saveConf = input("Save code (Y/n)").upper().strip()
                                if saveConf == "Y":
                                    progBar = ""
                                    for i in range(20):
                                        progBar += "#"
                                        print(f"[{progBar}]", end="\r", flush=True)
                                        time.sleep(0.1)
                                    print("\n")
                                    print("__________________________________")
                                    with open(filePath, "w", encoding='utf-8') as f:
                                        f.write("\n".join(newCode))   
                        else:
                            return
                    else:
                        print("##### INVALID FILE PATH #####")
            elif commEntered == "editor--new":
                fileNew = input("Enter the new file's path\n").strip()
                print("_____________________________")
                if fileNew.upper().startswith("C:"):
                    if not os.path.exists(fileNew):
                        newCode = []
                        count = 0
                        while True:
                            codeLnNew = input("Enter the code you want to save to the file (press cl to stop editing)\n")
                            print("_______________________________")
                            if codeLnNew == "cl":
                                break
                            count += 1
                            newCode.append(f"{count} {codeLnNew}")
                        progBar = ""
                        for i in range(20):
                            progBar += "#"
                            print(f"[{progBar}]", end="\r", flush=True)
                            time.sleep(0.1)
                        print("\n")
                        with open(fileNew, "w", encoding='utf-8') as f:
                            f.write("\n".join(newCode))
                else:
                    print("### INVALID FILE PATH ###")
            elif commEntered == "editor--read":
                filePathRead = input("Enter the file path to be opened.\n").upper().strip()
                print("_______________________________")
                if filePathRead.startswith("C:"):
                    if os.path.exists(filePathRead):
                        with open(filePathRead, "r", encoding='utf-8') as f:
                            codeOpened = f.read()
                        print(codeOpened)
                        print("_______________________________")
                else:
                    print("### INVALID FILE PATH ###")
            elif commEntered == "editor--quit":
                progBarQuit = ""
                for i in range(20):
                    progBarQuit += "#"
                    print(f"[{progBarQuit}] [Quitting editor...]", end="\r", flush=True)
                    time.sleep(0.1)
                print("\n")
                return
            elif commEntered=="editor--help":
                print(help)
            elif commEntered=="editor--info":
                print(info)
        else:
            print(" ### INVALID COMMAND ###")
