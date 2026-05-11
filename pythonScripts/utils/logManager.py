import os
from datetime import datetime as dt
import time
userProfile=os.environ["USERPROFILE"]
date=dt.now().astimezone().date()
def dirGen():
    if not os.path.exists(f"{userProfile}\\Desktop\\logs\\"):
        os.makedirs(f"{userProfile}\\Desktop\\logs\\")
        print("### DIRECTORY GENERATED ###")
def logsManager():
    dirGen()
    if not os.path.exists(f"{userProfile}\\Desktop\\logs\\task{date.strftime("%d.%M.%Y")}"):
     with open(f"{userProfile}\\Desktop\\logs\\log{date}.txt", "w", encoding='utf-8') as f:
         f.write(f"LOG {date}\n")
    commandsGlobal=["logManager--new", "logManager--view", "logManager--quit", "logManager--delete", "logManager--addLog"]
    def commands(commandsArg):
        print("##### COMMANDS #####")
        print("______________________")
        print(commandsArg)
    commands(commandsGlobal)
    while True:
        commandEnt=input("Enter a command.\n").strip()
        if commandEnt in commandsGlobal:
            if commandEnt == commandsGlobal[0]:
               log=[]
               while True:
                logSingle=input("Enter the log you want to make. Type cl to exit.\n").strip()
                print("______________________")
                if logSingle=="cl":
                  break
                log.append(logSingle)
               with open(f"{userProfile}\\Desktop\\logs\\log{date}.txt", "a", encoding='utf-8') as f:
                   f.write("\n".join(log)+"\n")
            elif commandEnt==commandsGlobal[1]:
                if len(os.listdir(f"{userProfile}\\Desktop\\logs\\"))==0:
                  print("Log directory is empty.").strip()
                else:
                    listOfPaths=os.listdir(f"{userProfile}\\Desktop\\logs\\")
                    print(listOfPaths)
                    print("______________________")
                    viewingLog=input("Enter a log to view.\n").strip().strip()
                    progBarProcess=""
                    if viewingLog in listOfPaths:
                      for i in range(20):
                        progBarProcess += "#"
                        print(f"[{progBarProcess}] [Processing file...]", end="\r", flush=True)
                        time.sleep(0.1)
                      print("\n")
                      with open(f"{userProfile}\\Desktop\\logs\\{viewingLog}", "r", encoding='utf-8') as f:
                         viewLog=f.read()
                      print("### REQUESTED LOG ###")
                      print("______________________")
                      print(f"### {viewingLog} ###")
                      print("______________________")
                      print("\n")
                      print(viewLog)
                    else:
                       print("### INVALID PATH ###")
            elif commandEnt=="logManager--delete":
                if len(os.listdir(f"{userProfile}\\Desktop\\logs\\"))==0:
                  print("Log directory is empty.").strip()
                else:
                   deletablePaths=os.listdir(f"{userProfile}\\Desktop\\logs\\")
                   print(deletablePaths)
                   print("______________________")
                   deletingLog=input("Enter a log to delete")
                   if deletingLog in deletablePaths:
                      os.remove(f"{userProfile}\\Desktop\\logs\\{deletingLog}")
            elif commandEnt=="logManager--quit":
                progBarQuit = ""
                for i in range(20):
                 progBarQuit += "#"
                 print(f"[{progBarQuit}] [Quitting Log Manager...]", end="\r", flush=True)
                 time.sleep(0.1)
                print()
                return
            elif commandEnt=="logManager--addLog":
               editableLogs=os.listdir(f"{userProfile}\\Desktop\\logs\\")
               if len(editableLogs)!=0:
                  print(editableLogs,"\n")
                  print("__________________")
                  print("\n")
                  logToBeAdded=input("Enter the name of the log\n") if len(editableLogs)==1 else input("Enter a log's name\n")
                  if logToBeAdded not in editableLogs:
                     print("### INVALID LOG PATH ###")
                  addLogPath=f"{userProfile}\\Desktop\\logs\\{logToBeAdded}"
                  addLogs=[]
                  while True:
                    addLog=input("Enter a log. Press cl to exit.\n")
                    print("__________________")
                    if addLog=="cl":
                       break
                    addLogs.append(addLog)
                  with open(addLogPath, "a", encoding='utf-8') as f:
                     f.write("\n\n".join(addLogs)+"\n")
                  print("### LOG SUCCESSFULLY ADDED ###")

        else:
            print("### INVALID COMMAND ###") 

logsManager()       
               
            
        
