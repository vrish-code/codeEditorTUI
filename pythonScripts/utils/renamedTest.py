from dotenv import load_dotenv
import os
load_dotenv()
apiKey=os.getenv('APIKEY')
print(apiKey)