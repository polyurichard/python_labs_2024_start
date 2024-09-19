import streamlit as st

# initialize session state for storing user input
if 'text_history' not in st.session_state:
    st.session_state.text_history = []

# Create a text input field
text_input = st.text_input('Enter some text', 'Type here...')
# Create a button
submit_button = st.button('Submit')
if submit_button:
    st.write('You entered:', text_input)
    st.session_state.text_history.append(text_input)
    st.session_state.input_box = "" # clear the input box


# Create a clear button
clear_button = st.button('Clear history')
if clear_button:
    st.session_state.text_history = []

# Display the history
st.write('History:')
for text in st.session_state.text_history:
    st.write(text)
