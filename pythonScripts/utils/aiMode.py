import requests as r
import os
from dotenv import load_dotenv
userProfile=os.environ["USERPROFILE"]
load_dotenv()
apiKey=os.getenv("APIKEY")
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

      for i in range(len(pathsForContext)):
         with open(pathsForContext[i], "r") as f:
            readList.append(f.read()) 
      print("______________________")
      print(f" 👤: {prompt}\n")
      realPrompt=f"Prompt:{prompt}, here's some code data in an array for context {readList}. If the array doesnt have anything, just skip it and do what the prompt tells you to. Always use British English."
      response=r.post("https://openrouter.ai/api/v1/chat/completions", headers={"Authorization":f"Bearer {apiKey}", "Content-Type":"application/json"}, json={
                        "model": "liquid/lfm-2.5-1.2b-instruct:free",
                        "messages": [{"role": "user", "content": realPrompt}],
                    }
                )
      data=response.json()
      print(f" 🤖: {data['choices'][0]['message']['content']}")  
