from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSES
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(YouAsk):
    response = model.generate_content(YouAsk)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Q & A with your assistant", layout="wide", initial_sidebar_state="expanded")

# Add a title and description
st.title("Smart C-assistant")
st.write("Ask questions and get responses from the Smart Chat-assistant")

# Main function to handle the app flow
def main():
    st.header("Start Chat...")

    # Initialize session state to store the previous questions and answers
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'responses' not in st.session_state:
        st.session_state.responses = []
    if 'current_input' not in st.session_state:
        st.session_state.current_input = ""

    # Display all previous questions and responses
    for i in range(len(st.session_state.questions)):
        st.subheader(f"You Ask {i+1}:")
        st.write(st.session_state.questions[i])
        st.subheader("Response:")
        st.write(st.session_state.responses[i])

    # Input section for the current question
    st.session_state.current_input = st.text_input("Input your question:", value=st.session_state.current_input, key="input_question")
    
    if st.button("Submit"):
        if st.session_state.current_input:
            response = get_gemini_response(st.session_state.current_input)
            st.session_state.questions.append(st.session_state.current_input)
            st.session_state.responses.append(response)
            st.session_state.current_input = ""  # Clear the input field after submission
            st.experimental_rerun()  # Re-run the script to update the UI

if __name__ == "__main__":
    main()

