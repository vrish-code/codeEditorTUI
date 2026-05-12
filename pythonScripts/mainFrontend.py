from utils import aiMode as aim
from utils import fileOperations as fop
from utils import logManager as lm
from utils import editor as ed


def main():
    info="""### TERM-CODE ###
            ____________________________________________
            This is a terminal based code editor with many modern features. 
            It has a CLI built from scratch in python.\n"""
    
    choiceList=["term-code --edit", "term-code --help", 
                "term-code --info", "term-code --exit", 
                "term-code --codeAssist", "term-code --fileOperations",
                "term-code --logManager"]
    print(choiceList)
main()
    
