import os
import time

def codeEditor():
    commandsGlobal=["editor --open", "editor --new", "editor --quit", "read"]
    def commandMode(commands):
        print("___________________________________")
        print("##### COMMANDS #####")
        print(commands)
        print("_______________________")
    commandMode(commandsGlobal)
    commEntered=input("Enter a command\n").strip()
    if commEntered in commandsGlobal:
     if commEntered=="editor --open":
        filePath=input("Enter the file path to be opened.\n").upper().strip()
        print("_______________________________")
        if filePath.startswith("c:") or filePath.startswith("C:"):
            if os.path.exists(filePath):
                with open(filePath, "r",encoding='utf-8') as f:
                    codeOpened=f.read()
                print(codeOpened)
                print("_______________________________")

                codeEdit=input("Edit code (press cl to stop editing)? (Y/n)").upper().strip()
                if codeEdit=="Y":
                    newCode=[]
                    while True:
                        codeLn=input()
                        if codeLn=="cl":
                            break
                        newCode.append(codeLn)
                    if newCode:
                        saveConf=input("Save code (Y/n)").upper().strip()
                        if saveConf=="Y":
                            progBar=""
                            for i in range(20):
                                progBar+="#"
                                print(f"[{progBar}]", end="\r", flush=True)
                                time.sleep(0.1)
                            print("\n")
                            print("__________________________________")
                            with open(filePath,"w", encoding='utf-8') as f:
                                f.write("\n".join(newCode))   
                            commandModeGoBack=input("Go back to command mode? (Y/n)").upper().strip()
                            print("_______________________________")
                            if commandModeGoBack=="Y":
                                commandMode(commandsGlobal)
                            else:quit()
                        else:
                            pass
                else:
                    quit()
            else:
                print("##### INVALID FILE PATH #####")
     elif commEntered=="editor --new":
         fileNew=input("Enter the new file's path\n").strip()
         print("_____________________________")
         if fileNew.startswith("c:") or fileNew.startswith("C:"):
             if not os.path.exists(fileNew):
                newCode=[]
                count=0
                while True:
                  codeLnNew=input("Enter the code you want to save to the file (press cl to stop editing)\n")
                  print("_______________/________________")
                  if codeLnNew=="cl":
                    break
                  count+=1
                  newCode.append([count, codeLnNew])
                progBar=""
                for i in range(20):
                    progBar+="#"
                    print(f"[{progBar}]", end="\r", flush=True)
                    time.sleep(0.1)
                print("\n")
                with open(fileNew,"w", encoding='utf-8') as f:
                    f.write("\n".join(newCode))
             else:
                 commChoice=("File path already exists. Go back to command mode to restart operation. (Y/n)").upper()
                 if commChoice=="Y":
                     commandMode(commandsGlobal)
                 else:
                     quit()
         else:
          print("### INVALID FILE PATH ###")
     elif commEntered=="read":
        filePathRead=input("Enter the file path to be opened.\n").upper().strip()
        print("_______________________________")
        if filePathRead.startswith("c:") or filePathRead.startswith("C:"):
            if os.path.exists(filePathRead):
                with open(filePathRead, "r",encoding='utf-8') as f:
                    codeOpened=f.read()
                print(codeOpened)
                print("_______________________________")
        else:
          print("### INVALID FILE PATH ###")
     elif commEntered=="editor --quit":
        progBarQuit=""
        for i in range(20):
            progBarQuit+="#"
            print(f"[{progBarQuit}] [Quitting editor...]" , end="\r", flush=True)
            time.sleep(0.1)
        print()
        return
    else:
        print(" ### INVALID COMMAND ###")
    
  

codeEditor()
                 
































