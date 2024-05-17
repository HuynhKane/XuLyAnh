import streamlit as st
import time
import numpy as np


import streamlit as st

# Tạo một component HTML tùy chỉnh
navbar = """
    <style>
        .navbar {
            background-color: #333;
            padding: 10px;
            color: white;
            text-align: center;
        }
    </style>
    <div class="navbar">
        <h2>Xử lý ảnh</h2>
    </div>
"""

# Hiển thị navbar sử dụng components
st.markdown(navbar, unsafe_allow_html=True)

# Các phần khác của ứng dụng Streamlit ở đây
st.title("Hello world")

