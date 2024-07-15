import altair as alt
import pandas as pd
import streamlit as st

# Show the page title and description.
st.set_page_config(page_title="Movies dataset", page_icon="🎬")
st.title("🎬 Movies dataset")
st.write(
    """
    This app visualizes data from [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    It shows which movie genre performed best at the box office over the years. Just 
    click on the widgets below to explore!
    """
)


# Load the Excel file
@st.cache_data
def load_data():
    file_path = 'data/shrimpcontract.csv'
    return pd.read_excel(file_path, sheet_name='Sheet1').ffill()

# Main application
def main():
    st.title("Sales Data Management")
    
    # Load data
    df = load_data()
    
    # Display the dataframe
    st.write("### Sales Data", df)
    
    # Add sidebar filters
    st.sidebar.title("Filters")
    date_filter = st.sidebar.date_input("签约日期", [])
    buyer_filter = st.sidebar.multiselect("买方名称", options=df["买方名称"].unique())
    
    # Apply filters
    if date_filter:
        df = df[df["签约日期"].isin(date_filter)]
    if buyer_filter:
        df = df[df["买方名称"].isin(buyer_filter)]
    
    # Display filtered dataframe
    st.write("### Filtered Sales Data", df)
    
    # Option to download the filtered data
    st.write("### Download Filtered Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name='filtered_sales_data.csv',
        mime='text/csv',
    )

if __name__ == "__main__":
    main()
