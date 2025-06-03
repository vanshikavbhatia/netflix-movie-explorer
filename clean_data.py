import pandas as pd

df = pd.read_csv("netflix_titles.csv")

# Drop rows with too many missing values
df = df.dropna(subset=["director", "cast", "country", "date_added", "rating", "duration"])

# Fill missing values with placeholders (optional)
# df["director"].fillna("Unknown", inplace=True)

# Save cleaned data
df.to_csv("netflix_cleaned.csv", index=False)

print("✅ Data cleaned and saved as netflix_cleaned.csv")
