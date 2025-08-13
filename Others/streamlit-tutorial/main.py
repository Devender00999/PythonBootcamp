import streamlit as st

# # Title and text
# st.title("My First Streamlit App")
# st.write("Hello! 👋 This is a quick Streamlit demo.")

# # Input
# name = st.text_input("Enter your name:")

# def print_name():
#    if pdf:
#       print(pdf.readlines())

# pdf = st.file_uploader('Upload PDF', type='pdf')
# st.button('Click Me!', on_click=print_name)

import streamlit as st
import numpy as np
import pandas as pd

# st.title("Dynamic Chart Example")
st.markdown("- Hello")

st.selectbox("Please select", options=["Option 1", "Option 2"])
# rows = st.slider("Number of rows", 5, 50, 10)
# data = pd.DataFrame(
#     np.random.randn(rows, 3),
#     columns=["A", "B", "C"]
# )
# st.line_chart(data)
st.dataframe(data=[{ "name": "Andrew", "email": "andrew@gmail.com"}, { "name": "benjemin", "email": "benjemin@gmail.com"}])

if st.button("Go to Page 2"):
    st.switch_page("pages/new.py")  # Path relative to main app file