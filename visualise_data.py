import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_cleaned.csv")

# Plot: Number of shows per country (Top 10)
top_countries = df['country'].value_counts().head(10)
top_countries.plot(kind='bar', title="Top 10 Countries Producing Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()
