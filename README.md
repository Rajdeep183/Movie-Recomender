# 🎬 MovieFlix - AI Movie Recommender

A sophisticated movie recommendation system built with Streamlit and machine learning algorithms. This application provides personalized movie recommendations based on content similarity using advanced natural language processing techniques.

## ✨ Features

- **🎯 Personalized Recommendations**: Get tailored movie suggestions based on your selected movies
- **🔍 Smart Search**: Quickly find movies with intelligent search functionality
- **📊 Interactive Dashboard**: Beautiful Netflix-inspired UI with modern design
- **📈 Data Visualization**: View recommendation statistics and insights
- **💾 Export Functionality**: Download your recommendations as CSV files
- **🎭 Movie Discovery**: Browse through a comprehensive movie database

## 🚀 Technologies Used

- **Frontend**: Streamlit with custom CSS styling
- **Backend**: Python with Pandas and NumPy
- **Machine Learning**: Content-based filtering using similarity algorithms
- **Data**: TMDB 5000 Movie Dataset
- **Styling**: Netflix-inspired dark theme with glassmorphism effects

## 📁 Project Structure

```
recomender/
├── recomender/                 # Data and Jupyter notebook
│   ├── movrec.ipynb           # Movie recommendation analysis
│   ├── tmdb_5000_movies.csv   # Movie dataset
│   └── tmdb_5000_credits.csv  # Credits dataset
├── streamlit-app/             # Streamlit application
│   ├── src/
│   │   ├── app.py            # Main application file
│   │   ├── utils/            # Utility modules
│   │   └── components/       # UI components
│   ├── requirements.txt      # Python dependencies
│   └── config.toml          # Streamlit configuration
└── README.md                 # Project documentation
```

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rajdeep183/recomender.git
   cd recomender
   ```

2. **Install dependencies**:
   ```bash
   cd streamlit-app
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run src/app.py
   ```

## 📊 Dataset

This project uses the TMDB 5000 Movie Dataset which includes:
- **Movies Dataset**: 5000 movies with metadata (genres, keywords, overview, etc.)
- **Credits Dataset**: Cast and crew information for each movie

## 🎯 How It Works

1. **Data Processing**: The system processes movie metadata and creates feature vectors
2. **Similarity Calculation**: Uses cosine similarity to find movies with similar characteristics
3. **Recommendation Generation**: Returns top-N most similar movies based on content features
4. **User Interface**: Provides an intuitive interface for movie selection and recommendation viewing

## 🌟 Key Features

### Movie Recommendation Engine
- Content-based filtering algorithm
- Similarity scoring based on multiple features
- Configurable number of recommendations (1-10)

### Modern UI/UX
- Netflix-inspired dark theme
- Responsive design with glassmorphism effects
- Interactive movie cards and search functionality
- Real-time search with auto-suggestions

### Data Export
- Download recommendations as CSV
- Detailed similarity scores included
- Easy data sharing and analysis

## 🚀 Usage

1. **Search for Movies**: Use the search bar to find your favorite movies
2. **Select a Movie**: Choose from the dropdown or browse the collection
3. **Set Preferences**: Adjust the number of recommendations you want
4. **Get Recommendations**: Click the "Get AI Recommendations" button
5. **Explore Results**: View similar movies with similarity scores
6. **Export Data**: Download your recommendations for future reference

## 🔧 Configuration

The application can be configured through:
- `streamlit-app/config.toml`: Streamlit-specific settings
- `streamlit-app/requirements.txt`: Python dependencies
- Custom CSS styling in `app.py` for UI customization

## 📈 Future Enhancements

- [ ] Add collaborative filtering
- [ ] Implement user rating system
- [ ] Include movie trailers and posters
- [ ] Add genre-based filtering
- [ ] Implement user accounts and history
- [ ] Add more recommendation algorithms

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Rajdeep Roy**
- GitHub: [@Rajdeep183](https://github.com/Rajdeep183)

## 🙏 Acknowledgments

- TMDB for providing the movie dataset
- Streamlit team for the amazing framework
- The open-source community for inspiration and tools

---

⭐ If you found this project helpful, please give it a star on GitHub!