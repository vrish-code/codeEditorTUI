import os
import time

def commandModeEditor():
    commandsGlobal=["editor --open", "editor --new", "editor --quit"]
    def commandMode(commands):
        print("___________________________________")
        print("##### COMMANDS #####")
        print(commands)
        print("_______________________")
    commandMode(commandsGlobal)
    commEntered=input("Enter a command")
    if commEntered in commandsGlobal:
     if commEntered=="editor --open":
        filePath=input("Enter the file path to be opened.")
        print("_______________________________")
        if filePath.startswith("c:" "C:"):
            if os.path.exists(filePath):
                with open(filePath, "r",encoding='utf-8') as f:
                    codeOpened=f.read()
                print(codeOpened)
                codeEdit=input("Edit code (press cl to stop editing)? (Y/n)").upper
                print("_______________________________")()
                if codeEdit=="Y":
                    newCode=[]
                    while True:
                        codeLn=input(codeEdit)
                        if codeLn=="cl":
                            break
                        newCode.append(codeLn)
                    if newCode:
                        saveConf=input("Save code (Y/n)").upper()
                        if saveConf=="Y":
                            progBar=""
                            for i in range(20):
                                progBar+="#"
                                print(f"[{progBar}]", end="\r", flush=True)
                                time.sleep(0.1)
                            print("__________________________________")
                            with open(filePath,"w", encoding='utf-8') as f:
                                f.write("\n".join(newCode))
                            commandModeGoBack=input("Go back to command mode? (Y/n)").upper()
                            print("_______________________________")
                            if commandModeGoBack=="Y":
                                commandMode()
                            else:quit()
                        else:
                            pass
                else:
                    quit()
     elif commEntered=="editor --new":
         fileNew=input("Enter the new file's path")
         print("_____________________________")
         if fileNew.startswith("c:" "C:"):
             if not os.path.exists(fileNew):
                newCode=[]
                while True:
                  codeLnNew=input("Enter the code you want to save to the file (press cl to stop editing)")
                  print("_______________________________")
                  if codeLnNew=="cl":
                    break
                  newCode.append(codeLnNew)
                newCode.remove("cl")
                for i in range(20):
                    progBar+="#"
                    print(f"[{progBar}]", end="\r", flush=True)
                    time.sleep(0.1)
                    with open(fileNew,"w", encoding='utf-8') as f:
                     f.write("\n".join(newCode))
             else:
                 commChoice=("File path already exists. Go back to command mode to restart operation. (Y/n)").upper()
                 if commChoice=="Y":
                     commandMode()
                 else:
                     quit()
commandModeEditor()
                 
































