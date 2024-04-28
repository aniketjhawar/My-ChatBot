import google.generativeai as gpt
prompt = input("Write your Prompt")
gpt.configure(api_key='AIzaSyAObqzeprhQ3olxjfxCGqT12k2ne0i3z9U')
geminipro = gpt.GenerativeModel('gemini-pro')
response = geminipro.generate_content(prompt)
print(response.text)