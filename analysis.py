# Import libraries
import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

print("\n✅ Dataset Loaded Successfully\n")

# -------------------------------
# 1. Basic Info
print(" Dataset Shape:")
print(df.shape)

print("\n📌 Columns:")
print(df.columns)

print("\n📌 Data Types:")
print(df.dtypes)

# -------------------------------
# 2. Missing Values
print("\n📌 Missing Values:")
print(df.isnull().sum())

# -------------------------------
# 3. Data Cleaning
df.drop_duplicates(inplace=True)
df.fillna("Unknown", inplace=True)

# Convert date
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

print("\n✅ Data Cleaning Done")

# -------------------------------
# 4. Analysis

# Movies vs TV Shows
print("\n🎬 Movies vs TV Shows:")
print(df['type'].value_counts())

# Content added per year
print("\n📅 Content Release Year Trend:")
print(df['release_year'].value_counts().sort_index().tail(10))

# Top 10 Countries
print("\n🌍 Top 10 Countries:")
print(df['country'].value_counts().head(10))

# Top 10 Genres
print("\n🎭 Top 10 Genres:")
genres = df['listed_in'].str.split(',').explode()
print(genres.value_counts().head(10))

# Top Ratings
print("\n⭐ Ratings Distribution:")
print(df['rating'].value_counts().head(10))

# -------------------------------
# 5. Save Cleaned Data (Important)
df.to_csv("cleaned_netflix_data.csv", index=False)

print("\n💾 Cleaned dataset saved as 'cleaned_netflix_data.csv'")

# -------------------------------
# 6. Key Insights (Auto Print)

print("\n📊 Key Insights:")

movies = df[df['type'] == 'Movie'].shape[0]
tvshows = df[df['type'] == 'TV Show'].shape[0]

print(f"➡️ Total Movies: {movies}")
print(f"➡️ Total TV Shows: {tvshows}")

top_country = df['country'].value_counts().idxmax()
print(f"➡️ Top Content Producing Country: {top_country}")

top_genre = genres.value_counts().idxmax()
print(f"➡️ Most Popular Genre: {top_genre}")

top_rating = df['rating'].value_counts().idxmax()
print(f"➡️ Most Common Rating: {top_rating}")

print("\n🚀 Analysis Completed Successfully!")