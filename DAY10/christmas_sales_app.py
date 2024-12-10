import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
@st.cache_data
def load_data():
    data = pd.read_csv('data.csv')
    # Convert 'Sales' and 'Units_Sold' to numeric format
    #data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')  # Convert to numeric, set invalid to NaN
    #data['Units_Sold'] = pd.to_numeric(data['Units_Sold'], errors='coerce')  # Convert to numeric, set invalid to NaN
    
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y', dayfirst=True) # Convert 'Date' column to datetime
    data['Year'] = data['Date'].dt.year #Extract Year for filter
    return data

data = load_data()

# Sidebar filters
st.sidebar.header("Filters")

selected_year = st.sidebar.selectbox("Select Year", sorted(data['Year'].unique()))

start_date = st.sidebar.date_input("Start Date", data['Date'].min())
end_date = st.sidebar.date_input("End Date", data['Date'].max())

product_type = st.sidebar.multiselect("Select Product Type", data['Product_Type'].unique(), default=data['Product_Type'].unique())

selected_region = st.sidebar.multiselect("Select Region", data['Region'].unique(), data['Region'].unique())

# Apply Filters
filtered_data = data[(data['Year'] == selected_year) &
                    (data['Date'] >= pd.to_datetime(start_date)) &
                    (data['Date'] <= pd.to_datetime(end_date)) &
                    (data['Product_Type'].isin(product_type)) &
                    (data['Region'].isin(selected_region))]

# Main dashboard
st.title("🎄 Christmas Sales Dashboard 🎄")
st.markdown("Analyze sales performance across stores, product types, and regions with interactive charts and filters.")
st.write(f"Data for {selected_year}")

# Display Filtered Data
#st.subheader("Filtered Data")
#st.dataframe(filtered_data)

# Visualizations

# Dynamic Scorecards
st.subheader("📊 Scorecards")
total_sales = filtered_data['Sales'].sum()
total_units_sold = filtered_data['Units_Sold'].sum()
st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Total Units Sold", f"{total_units_sold:,}")

# Regional Performance
st.subheader("Sales by Region")
fig, ax = plt.subplots()
filtered_data.groupby('Region')['Sales'].sum().plot(kind='bar', ax=ax, color='green')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.title('Sales by Region')
st.pyplot(fig)

# Sales by Product Type
st.subheader("Sales by Product Type")
sales_by_product = filtered_data.groupby('Product_Type')['Sales'].sum()
st.bar_chart(sales_by_product)

# Daily Sales Trend
st.subheader("Daily Sales Trend")
daily_sales = filtered_data.groupby('Date')['Sales'].sum()
st.line_chart(daily_sales)

# Top Performing Stores
st.subheader("Top Performing Stores")
sales_by_store = filtered_data.groupby('Store')['Sales'].sum().sort_values(ascending=False).head(10)
st.bar_chart(sales_by_store)

# Footer
st.markdown("### 🎄 Happy Holidays! 🎄")