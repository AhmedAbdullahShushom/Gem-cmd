import sys
if len(sys.argv) > 1:
    upt = " ".join(sys.argv[1:]) 
else:
    print("No argument provided")
    upt = str(input("prompt:")) 
if len(upt)<3:
   quit()

import google.generativeai as genai
geminikey = "your ai key"
genai.configure(api_key=geminikey)
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(upt)
print(response.text)

input("")
