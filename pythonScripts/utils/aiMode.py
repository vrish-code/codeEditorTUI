import requests as r
import os
from dotenv import load_dotenv
userProfile=os.environ["USERPROFILE"]
load_dotenv()
apiKey=os.getenv("API-KEY")
def aiMode():
    while True:
     prompt=input("Enter a prompt.\n")
     pathsForContext=[]
     while True:
        pathForContext=input("Enter a file path for context. Press cl to exit.\n")
        print("___________________")
        if pathForContext=="cl":
           break
        pathsForContext.append(pathForContext)
     readList=[]
     if len(pathsForContext)!=0:
        for i in range(len(pathsForContext)):
            with open(pathsForContext[i], "r") as f:
              readList.append(f.read()) 
        print("______________________")
        print(f" 👤: {prompt}")
        realPrompt=f"Prompt:{prompt}, here's some code data in an array for context {readList}"
        response=r.post("https://openrouter.ai/api/v1/chat/completions", headers={"Authorization":f"Bearer {apiKey}", "Content-Type":"application/json"}, json={
                        "model": "openrouter/free",
                        "messages": [{"role": "user", "content": realPrompt}],
                    },
                )
        print(f" 🤖: {response.json()['choices'][0]['message']['content']}")
aiMode()