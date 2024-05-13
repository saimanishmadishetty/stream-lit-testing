import streamlit as st
import pandas as pd
import numpy as np

# Generate sample data
data = pd.DataFrame({
    'first_column': np.arange(1, 11),
    'second_column': np.random.randn(10)
})

# Set a title for your Streamlit app
st.title('Data Analysis with Streamlit')

# Display the DataFrame with a title
st.write("Here's our first attempt at using data to create a table:")
st.write(data)

# Plot a line chart with a title
st.subheader('Line Chart')
st.line_chart(data)
