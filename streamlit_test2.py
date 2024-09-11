import streamlit as st

# 初始化 session_state
if 'text_history' not in st.session_state:
    st.session_state.text_history = []

# 创建文本输入框
text_input = st.text_input("请输入一些文本:")

# 创建提交按钮
submit_button = st.button("提交")
if submit_button:
    st.session_state.text_history.append(text_input)
    st.write("您输入的是:", text_input)
    text_input = ""  # 清空输入框

# 创建清除历史按钮
clear_button = st.button("清除历史")
if clear_button:
    st.session_state.text_history = []

# 显示过去提交的输入
st.write("## 过去的输入")
for text in st.session_state.text_history:
    st.write(text)