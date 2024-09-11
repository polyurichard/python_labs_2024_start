import streamlit as st

# 设置应用程序标题
st.title("简单的Streamlit应用程序")

# 显示文本输入框
user_input = st.text_input("请输入一些文本:")

# 显示用户输入的文本
st.write("您输入的文本是:", user_input)

# 显示一个按钮
if st.button("点击我"):
    st.write("按钮已被点击！")