# Import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('dark_background')

# Page config
st.set_page_config(page_title="Netflix Dashboard", layout="wide")
st.markdown("""
<style>
.card {
    background-color: #1F1F1F;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.5);
    margin-bottom: 20px;
}
.card-title {
    color: #E50914;
    font-size: 20px;
    font-weight: bold;
}
.card-value {
    color: white;
    font-size: 28px;
}
</style>
""", unsafe_allow_html=True)

# Load cleaned dataset
df = pd.read_csv("cleaned_netflix_data.csv")

# Title
st.title("📺 Netflix / OTT Data Analysis Dashboard")
st.subheader("🎬 Netflix Insights")

col1, col2, col3 = st.columns(3)

movies = df[df['type'] == 'Movie'].shape[0]
tvshows = df[df['type'] == 'TV Show'].shape[0]
total = df.shape[0]

with col1:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Total Titles</div>
        <div class="card-value">{total}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">Movies</div>
        <div class="card-value">{movies}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="card">
        <div class="card-title">TV Shows</div>
        <div class="card-value">{tvshows}</div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Sidebar Filters
st.sidebar.header("🔍 Filters")

type_filter = st.sidebar.selectbox("Select Type", df['type'].unique())

country_filter = st.sidebar.selectbox(
    "Select Country",
    sorted(df['country'].dropna().unique())
)

# Apply filters
filtered_df = df[
    (df['type'] == type_filter) &
    (df['country'] == country_filter)
]

# -------------------------------
# KPI Metrics
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Titles", df.shape[0])
col2.metric("Movies", df[df['type']=="Movie"].shape[0])
col3.metric("TV Shows", df[df['type']=="TV Show"].shape[0])

# -------------------------------
# Show filtered data
st.subheader("📄 Filtered Data")
st.dataframe(filtered_df.head(20))

# -------------------------------
# Charts Section

st.subheader("📊 Visual Insights")

col1, col2 = st.columns(2)

# 1. Content Type Distribution
with col1:
    st.write("### Content Type Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(x='type', data=df, ax=ax1)
    st.pyplot(fig1)

# 2. Top Countries
with col2:
    st.write("### Top 10 Countries")
    top_countries = df['country'].value_counts().head(10)
    st.bar_chart(top_countries)

# -------------------------------
# Second Row Charts

col3, col4 = st.columns(2)

# 3. Release Year Trend
with col3:
    st.write("### Content Over Years")
    year_data = df['release_year'].value_counts().sort_index()
    st.line_chart(year_data)

# 4. Top Genres
with col4:
    st.write("### Top Genres")
    genres = df['listed_in'].str.split(',').explode()
    top_genres = genres.value_counts().head(10)
    st.bar_chart(top_genres)

# -------------------------------
# Rating Distribution

st.subheader("⭐ Ratings Distribution")

rating_data = df['rating'].value_counts().head(10)
st.bar_chart(rating_data)

# -------------------------------
# Footer Insight Section

st.subheader("📌 Key Insights")

movies = df[df['type'] == 'Movie'].shape[0]
tvshows = df[df['type'] == 'TV Show'].shape[0]

top_country = df['country'].value_counts().idxmax()

genres = df['listed_in'].str.split(',').explode()
top_genre = genres.value_counts().idxmax()

top_rating = df['rating'].value_counts().idxmax()

st.write(f"🎬 Movies dominate the platform with {movies} titles.")
st.write(f"📺 TV Shows count: {tvshows}")
st.write(f"🌍 Most content is produced by: {top_country}")
st.write(f"🎭 Most popular genre: {top_genre}")
st.write(f"⭐ Most common rating: {top_rating}")

# -------------------------------
st.success("✅ Dashboard Loaded Successfully!")