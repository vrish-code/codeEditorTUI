import os
from datetime import datetime as dt, timezone as tz
class const:
    def __init__(self, value):
        self._value=value
    @property
    def makeConst(self):
        return self._value
userProfile=const(os.environ["USERPROFILE"])
dateAndTime=dt.now(tz.utc)
def dirGen():
    
    if not os.path.exists(f"C:/Users/{userProfile}/Desktop/log/"):
        os.makedirs(f"C:/Users/{userProfile}/Desktop/log/")
        print("### DIRECTORY GENERATED ###")
def logsManager():
    dirGen()
    if not os.path.exists(f"C:/Users/{userProfile}/Desktop/log/task{dateAndTime.strftime("%D.%M.%Y")}"):
     with open(f"C:/Users/{userProfile}/Desktop/log/task{dateAndTime.strftime("%D.%M.%Y")}.txt") as f:
         f.write()
    commandsGlobal=["log--new", "log--view", "log --quit", "log --delete"]
    def commands(commandsArg):
        print("##### COMMANDS #####")
        print("______________________")
        print(commandsArg)
    commands(commandsGlobal)
    while True:
        commandEnt=input("Enter a command.")
        if commandEnt in commandsGlobal:
            if commandEnt == commandsGlobal[0]:
               log=[]
               while True:
                logSingle=input("Enter the log you want to make. Type cl to exit.")
                if logSingle=="cl":
                  break
                log.append(logSingle)
               with open(f"C:/Users/{userProfile}/Desktop/log/task{dateAndTime.strftime("%D.%M.%Y")}.txt") as f:
                   f.write("\n".join(log))
                
               
            
        
