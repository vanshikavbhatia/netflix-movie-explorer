import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load data
df = pd.read_csv('netflix_titles.csv')

# Pie chart: Movies vs TV Shows
type_counts = df['type'].value_counts().reset_index()
type_counts.columns = ['type', 'count']
type_fig = px.pie(type_counts, names='type', values='count', title='Movies vs TV Shows')

# Bar chart: Top genres
genre_counts = df['listed_in'].str.split(', ', expand=True).stack().value_counts().head(10)
genre_fig = px.bar(genre_counts, x=genre_counts.index, y=genre_counts.values, labels={'x':'Genre', 'y':'Count'}, title='Top 10 Genres')

# Line chart: Releases over years
year_counts = df['release_year'].value_counts().sort_index()
year_fig = px.line(x=year_counts.index, y=year_counts.values, labels={'x':'Year', 'y':'Releases'}, title='Releases Over the Years')

# Bar chart: Average duration
duration_df = df[df['duration'].str.contains('min', na=False)]
duration_df['duration_int'] = duration_df['duration'].str.extract('(\d+)').astype(int)
avg_duration = duration_df.groupby('release_year')['duration_int'].mean().reset_index()
duration_fig = px.line(avg_duration, x='release_year', y='duration_int', labels={'release_year':'Year', 'duration_int':'Avg Duration (min)'}, title='Average Movie Duration Over Years')

# Show all charts in browser
type_fig.show()
genre_fig.show()
year_fig.show()
duration_fig.show()
