import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data
df = pd.read_csv("netflix_titles.csv")

# Title
st.title("📺 Netflix Movie & TV Show Explorer")

# Dataset overview
st.subheader("Dataset Overview")
st.write(df.head())

# Filter by type
st.sidebar.header("Filter")
selected_type = st.sidebar.multiselect("Select Type", df['type'].unique(), default=df['type'].unique())
filtered_df = df[df['type'].isin(selected_type)]

# Movies vs TV Shows
st.subheader("Distribution of Content Types")
type_counts = filtered_df['type'].value_counts().reset_index()
type_counts.columns = ['Type', 'Count']
fig1 = px.pie(type_counts, names='Type', values='Count', title='Movies vs TV Shows')
st.plotly_chart(fig1)

# Top Genres
st.subheader("Top Genres")
all_genres = df['listed_in'].str.split(', ').explode()
top_genres = all_genres.value_counts().nlargest(10).reset_index()
top_genres.columns = ['Genre', 'Count']
fig2 = px.bar(top_genres, x='Genre', y='Count', title='Top 10 Genres')
st.plotly_chart(fig2)

# Top Countries
st.subheader("Top Countries")
top_countries = df['country'].dropna().str.split(', ').explode().value_counts().nlargest(10).reset_index()
top_countries.columns = ['Country', 'Count']
fig3 = px.bar(top_countries, x='Country', y='Count', title='Top 10 Countries')
st.plotly_chart(fig3)

# Releases over the years
st.subheader("Content Releases Over the Years")
yearly_counts = df['release_year'].value_counts().sort_index().reset_index()
yearly_counts.columns = ['Year', 'Count']
fig4 = px.line(yearly_counts, x='Year', y='Count', title='Releases Over Time')
st.plotly_chart(fig4)

# Average duration
st.subheader("Average Duration")
duration_data = df[df['duration'].notnull()]
duration_data['duration_mins'] = duration_data['duration'].str.extract('(\d+)').astype(float)
avg_duration = duration_data.groupby('type')['duration_mins'].mean().reset_index()
fig5 = px.bar(avg_duration, x='type', y='duration_mins', title='Average Duration by Type')
st.plotly_chart(fig5)
