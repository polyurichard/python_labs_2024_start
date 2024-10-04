import streamlit as st

if 'test_history' not in st.session_state:
    st.session_state.test_history = []


text_input = st.text_input('Enter some text')

subnit_button = st.button("submit")
if subnit_button:
    st.session_state.test_history.append(text_input)
    
    st.write("you have submitted:", text_input)
    st.session_state.input_box = "" # Clear the input box

clear_button = st.button("clear history")
if clear_button:
    st.session_state.test_history = []
    st.write("history cleared")
st.write("Past inputs")
for test in st.session_state.test_history:
    st.write(test)