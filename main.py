#step1: Import packages
from dotenv import load_dotenv
import os
from google import genai

#step2: Load the variable in the .env file
load_dotenv()

#step3: Get the api key
api_key=os.getenv("GEMINI_API_KEY")

#step4: Check api loaded or not
if api_key:
    print("API key successfully loaded")
else:
    print("Key not found")

#step5: Create the client 
client=genai.Client(api_key=api_key)

#step6: Select the free tier model from the gemini model
model="gemini-3.8-flash"

#step7: Get the input from the user
user_input=input("Ask AI:")

#step8: Get the response from the AI model
response=client.models.generate_content(
    model=model,
    contents=user_input
)

#step9: print the response
print(response.text)