import streamlit as st  
import google.generativeai as gpt

gpt.configure(api_key='AIzaSyAObqzeprhQ3olxjfxCGqT12k2ne0i3z9U')
geminipro = gpt.GenerativeModel('gemini-pro')


def generate_response(prompt):
    if prompt:
        response = geminipro.generate_content(prompt)
        return response.text
    else:
        return "Please enter a prompt."

def main():
    st.title("My AI")
    prompt = st.text_input("Write your Prompt")
    if st.button("Generate Response"):
        generated_response = generate_response(prompt)
        st.text("Response :")
        st.write(generated_response)

if __name__ == '__main__':
    main()