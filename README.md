# 🎬 MovieFlix - AI Movie Recommender

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live%20Demo-red?logo=streamlit&logoColor=white)](https://recomender.streamlit.app/)
[![MIT License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

A state-of-the-art movie recommendation system that leverages advanced natural language processing and machine learning to deliver highly personalized movie suggestions. Built with Streamlit, MovieFlix offers a seamless, interactive, and visually striking user experience inspired by Netflix.

## ✨ Features

- **🎯 Personalized Recommendations:** Receive tailored movie suggestions based on your favorites.
- **🔍 Smart Search:** Instantly find movies using intelligent, real-time search with auto-suggestions.
- **📊 Interactive Dashboard:** Modern Netflix-inspired UI with responsive design and glassmorphism effects.
- **📈 Data Visualization:** Gain insights with visual statistics about your recommendations.
- **💾 Export Functionality:** Download your recommended movies, complete with similarity scores, as CSV files.
- **🎭 Movie Discovery:** Browse a rich database of 5000+ movies with detailed metadata.
- **⚡ Lightning Fast:** Real-time results powered by optimized content-based filtering.

## 🚀 Technologies Used

- **Frontend:** Streamlit, custom CSS, and glassmorphism design principles
- **Backend:** Python, Pandas, NumPy
- **Machine Learning:** Content-based filtering using cosine similarity and NLP feature extraction
- **Data Source:** [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Styling:** Netflix-inspired dark theme, fully responsive

## 📁 Project Structure

```
Movie-Recomender/
├── recomender/                 # Data analysis and Jupyter notebooks
│   ├── movrec.ipynb           # Movie recommendation analysis notebook
│   ├── tmdb_5000_movies.csv   # Main movies dataset
│   └── tmdb_5000_credits.csv  # Credits dataset
├── streamlit-app/             # Streamlit application
│   ├── src/
│   │   ├── app.py             # Main Streamlit app
│   │   ├── utils/             # Utility modules (preprocessing, similarity, etc.)
│   │   └── components/        # UI components (custom widgets, cards, etc.)
│   ├── requirements.txt       # Python dependencies
│   └── config.toml            # Streamlit configuration
└── README.md                  # Project documentation
```

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rajdeep183/Movie-Recomender.git
   cd Movie-Recomender
   ```

2. **Install dependencies:**
   ```bash
   cd streamlit-app
   pip install -r requirements.txt
   ```

3. **Launch the application:**
   ```bash
   streamlit run src/app.py
   ```

   The app will be available at [http://localhost:8501](http://localhost:8501).

## 📊 Dataset Overview

Utilizes the TMDB 5000 Movie Dataset, featuring:
- **Movies:** Over 5000 entries with genres, overviews, keywords, and more.
- **Credits:** Cast and crew metadata for deeper insights.

## 🎯 How It Works

1. **Data Processing:** Cleans and transforms movie metadata into feature-rich vectors.
2. **Similarity Calculation:** Computes cosine similarity to identify movies with shared characteristics.
3. **Recommendation Generation:** Returns the top-N most similar movies for any selected title.
4. **User Interface:** Engaging, interactive UI for effortless selection and exploration.

## 🌟 Key Features Breakdown

### Recommendation Engine
- Content-based filtering using NLP and metadata
- Multi-feature similarity scoring (genres, keywords, overview, cast)
- Configurable recommendation count (1-10)

### Modern UI/UX
- Netflix-style dark/glassy look
- Responsive layouts for desktop and mobile
- Live search with suggestions
- Animated movie cards and intuitive navigation

### Data Export
- Download recommendations as CSV
- Includes detailed similarity scores for transparency
- Easy sharing and offline analysis

## 🚀 Usage Guide

1. **Search for Movies:** Type in the search bar for instant suggestions.
2. **Select a Movie:** Pick a title or browse the curated collection.
3. **Set Preferences:** Choose how many recommendations you want.
4. **Get Recommendations:** One click, and your list appears.
5. **Explore Results:** View similar movies, hover for details and similarity scores.
6. **Export Data:** Download your recommendations for later use.

## 🔧 Configuration

- `streamlit-app/config.toml`: Streamlit-specific options (theme, layout, etc.)
- `streamlit-app/requirements.txt`: Python package dependencies
- Custom CSS can be found in `src/app.py` for further UI tweaks

## 📈 Planned Enhancements

- [ ] Collaborative filtering (user-to-user recommendations)
- [ ] User rating and feedback system
- [ ] Movie trailers and poster previews
- [ ] Genre and mood-based filters
- [ ] User accounts with recommendation history
- [ ] Multiple recommendation algorithms (hybrid, trending, etc.)

## 📄 License

This project is released under the [MIT License](LICENSE).

## 👨‍💻 Author

**Rajdeep Roy**  
[GitHub: @Rajdeep183](https://github.com/Rajdeep183)

## 🙏 Acknowledgments

- [TMDB](https://www.themoviedb.org/) for providing the open movie dataset
- [Streamlit](https://streamlit.io/) for an outstanding rapid application framework
- The open-source community for inspiration, modules, and best practices

---
