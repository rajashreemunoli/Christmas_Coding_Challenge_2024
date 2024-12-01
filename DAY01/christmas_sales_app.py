import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    data = pd.read_csv('data.csv')
    data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')  # Convert to numeric, set invalid to NaN
    return data

data = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_year = st.sidebar.selectbox("Select Year", data['Year'].unique())
selected_region = st.sidebar.multiselect("Select Region", data['Region'].unique(), data['Region'].unique())

# Filter data
filtered_data = data[(data['Year'] == selected_year) & (data['Region'].isin(selected_region))]

# Main dashboard
st.title("🎄 Christmas Tree Sales Dashboard 🎄")
st.write(f"Data for {selected_year}")
st.dataframe(filtered_data)

# Visualization
st.subheader("Sales by Region")
fig, ax = plt.subplots()
filtered_data.groupby('Region')['Sales'].sum().plot(kind='bar', ax=ax, color='green')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.title('Christmas Tree Sales by Region')
st.pyplot(fig)