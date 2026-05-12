from utils import aiMode as aim
from utils import fileOperations as fop
from utils import logManager as lm
from utils import editor as ed


def main():
    info = """\n### TERM-CODE INFO ###
____________________________________________
This is a terminal-based code editor with 
many modern features. It has a custom CLI 
built entirely from scratch in Python."""
    help = """### TERM-CODE HELP MENU ###
____________________________________________________

Available Commands:
  term-code --edit            Open the internal code editor environment.
  term-code --logManager      Launch the system log manager and tracker.
  term-code --codeAssist      Activate the AI programming assistant.
  term-code --fileOperations  Execute file and directory manipulation tools.
  term-code --help            Display this command overview menu.
  term-code --info            Show project details and system variables.
  term-code --version         Display current version build metadata.
  term-code --exit            Safely terminate the active terminal session.
____________________________________________________"""
    version="1.0.0"
    print("### TERM-CODE ###\n")
    print("______________________________")
    print("\t### COMMANDS ###")
    choices=""" 
        _________________________________________________________________
        term-code --edit\t term-code --logManager\t term-code --codeAssist\t term-code --fileOperations\n
        __________________________________________________________________
         term-code --help\t term-code --info\t term-code --version\t term-code --exit\t"""
    print("".join(choices))
    while True:
     command=input("Enter a command.\n")
     commandList=["term-code --edit", "term-code --logManager", "term-code --codeAssist", "term-code --fileOperations", 
                 "term-code --help", "term-code --info", "term-code --version", "term-code --exit"]
     if command not in commandList:
        print("### INVALID COMMAND ###")
     else:
        if command==commandList[0]:
           ed.codeEditor()
        elif command==commandList[1]:
           lm.logsManager()
        elif command==commandList[2]:
           aim.aiMode()
        elif command==commandList[3]:
           fop.fileOps()
        elif command==commandList[4]:
           print(help,"\n")
        elif command==commandList[5]:
           print(info, "\n")
        elif command==commandList[6]:
           print(version, "\n")
        else:
           quit()

        
if __name__=="__main__":
   main()

    
