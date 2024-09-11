import streamlit as st
import requests
import json

# 设置应用程序标题
st.title("实时天气信息")

# 获取天气数据
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# 检查请求是否成功
if result.status_code == 200:
    # 解析JSON响应
    result_dict = result.json()

    # 显示湿度信息
    humidity = result_dict['humidity']['data'][0]['value']
    st.write(f"当前湿度: {humidity}%")

    # 显示城市温度信息
    st.write("### 各城市温度")
    for city in result_dict['temperature']['data']:
        st.write(f"城市: {city['place']}, 温度: {city['value']}°C")

    # 将数据转换为表格形式
    city_data = [{"城市": city['place'], "温度 (°C)": city['value']} for city in result_dict['temperature']['data']]
    st.table(city_data)
else:
    st.write("无法获取天气数据，请稍后再试。")