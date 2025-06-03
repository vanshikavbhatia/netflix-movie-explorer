import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("netflix_titles.csv")
df.dropna(subset=['type', 'release_year', 'listed_in', 'country', 'duration'], inplace=True)

st.set_page_config(page_title="Netflix Movie Explorer", layout="wide")

st.title("🎬 Netflix Movie & TV Show Explorer")
st.markdown("Analyze Netflix content by type, genre, country, and more!")

# Sidebar Filters
st.sidebar.header("Filter Content")
type_options = st.sidebar.multiselect("Select Type", df["type"].unique(), default=df["type"].unique())
country_options = st.sidebar.multiselect("Select Country", df["country"].dropna().unique(), default=["United States"])
year_range = st.sidebar.slider("Select Release Year Range", int(df["release_year"].min()), int(df["release_year"].max()), (2010, 2021))
genre_input = st.sidebar.text_input("Filter by Genre (e.g. Drama, Comedy)")

# Apply filters
filtered_df = df[
    (df["type"].isin(type_options)) &
    (df["country"].isin(country_options)) &
    (df["release_year"].between(year_range[0], year_range[1]))
]

if genre_input:
    filtered_df = filtered_df[filtered_df["listed_in"].str.contains(genre_input, case=False)]

# --- Charts ---
col1, col2 = st.columns(2)

with col1:
    # Fix here: rename columns after reset_index()
    type_counts = filtered_df["type"].value_counts().reset_index()
    type_counts.columns = ['type', 'count']  # Rename columns properly
    fig1 = px.pie(type_counts, names="type", values="count", title="Distribution: Movies vs TV Shows")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    year_count = filtered_df["release_year"].value_counts().sort_index()
    fig2 = px.line(x=year_count.index, y=year_count.values, labels={'x':'Release Year', 'y':'Count'}, title="Content Releases Over the Years")
    st.plotly_chart(fig2, use_container_width=True)

# Genre Analysis
genre_data = df["listed_in"].str.split(", ", expand=True).stack().value_counts().reset_index()
genre_data.columns = ['Genre', 'Count']
top_genres = genre_data.head(10)
st.subheader("Top 10 Genres")
fig3 = px.bar(top_genres, x="Genre", y="Count", color="Genre", title="Most Common Genres on Netflix")
st.plotly_chart(fig3, use_container_width=True)

# Duration
st.subheader("Duration Distribution")
duration_df = filtered_df.copy()
duration_df['duration_int'] = duration_df['duration'].str.extract('(\d+)').astype(float)
fig4 = px.histogram(duration_df, x='duration_int', nbins=30, title="Duration Distribution")
st.plotly_chart(fig4, use_container_width=True)

# Data Table
st.subheader("Filtered Netflix Titles")
st.dataframe(filtered_df[['title', 'type', 'release_year', 'country', 'listed_in']].reset_index(drop=True))
