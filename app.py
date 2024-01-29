import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
file_path = 'C:\\Users\\HP\\Downloads\\WHO-COVID-19-global-table-data(1).csv'
df = pd.read_csv(file_path)

# Print column names for debugging
st.write("Column names in the Dataframe:", df.columns.tolist())

# Streamlit App
st.title("COVID-19 Dashboard")

# Sidebar - Country Selection
try:
    country = st.sidebar.selectbox("Select a Country", df["Country"].unique())
except Exception as e:
    st.error(f"Error: {e}")

#Display the DataFrame (for debugging purposes)
st.write(df)

# Sidebar - Metric Selection
metric_options= [
    "Cases - cumulative total", 
    "Cases - cumulative total per 100000 population",
    "Deaths - cumulative total",
    "Deaths - cumulative total per 100000 population",
]
metric = st.sidebar.selectbox("Select a Metric", metric_options)

# Filtering data for the selected country
filtered_data = df[df["Country"] == country]

# List of metrics to compare
metrics = [
    "Cases - cumulative total",
    "Cases - cumulative total per 100000 population", 
    "Deaths - cumulative total",
    "Deaths - cumulative total per 100000 population",
]

# Melt the DataFrame to transform it for the grouped bar chart
melted_data = filtered_data.melt(id_vars=["Country"], value_vars=metrics, var_name="Metric", value_name="Value")

st.write(melted_data)
if not melted_data.empty:
    fig = px.bar(
        melted_data, 
        x="Metric", 
        y="Value", 
        color="Metric",
        title=f"Comparison of Metrics for {country}"
    )
    st.plotly_chart(fig)
else:
    st.write("No data available to plot.")

# Display the figure
st.plotly_chart(fig)

# Displaying Data
if not filtered_data.empty:
    st.write(f"Data for {country}:")
    st.write(filtered_data[[metric]])
    # Optionally, you can add a bar chart or other plot types here
else:
    st.write(f"No data available for {country}")



