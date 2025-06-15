# MovieFlix - AI Movie Recommender System
# Last updated: June 14, 2025 - Fixed scikit-learn dependency issues

import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

# Import our custom modules
from utils import MovieRecommender
from components import (
    create_netflix_header, 
    create_movie_card_netflix, 
    create_search_dropdown_netflix,
    create_stats_cards_netflix,
    create_recommendation_chart_netflix,
    create_featured_section
)

# Configure Streamlit page
st.set_page_config(
    page_title="MovieFlix - AI Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Simple CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;900&display=swap');
    
    .main {
        background: linear-gradient(135deg, #0f0f23 0%, #1a0d1a 50%, #0d1117 100%);
        background-attachment: fixed;
        color: white;
        font-family: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #0f0f23 0%, #1a0d1a 50%, #0d1117 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Enhanced Sidebar Styling */
    .stSidebar {
        background: linear-gradient(180deg, rgba(15, 15, 35, 0.95) 0%, rgba(26, 13, 26, 0.98) 50%, rgba(13, 17, 23, 0.95) 100%);
        backdrop-filter: blur(30px);
        -webkit-backdrop-filter: blur(30px);
        border-right: 1px solid rgba(229, 9, 20, 0.2);
        box-shadow: 4px 0 25px rgba(0, 0, 0, 0.3);
    }
    
    .stSidebar > div {
        background: transparent;
        padding: 20px 15px;
    }
    
    /* Sidebar Header - Netflix Style */
    .sidebar-header {
        background: linear-gradient(135deg, rgba(229, 9, 20, 0.15) 0%, rgba(229, 9, 20, 0.05) 100%);
        padding: 25px 20px;
        margin: -20px -15px 30px -15px;
        border-bottom: 2px solid rgba(229, 9, 20, 0.2);
        text-align: center;
        backdrop-filter: blur(20px);
        position: relative;
        overflow: hidden;
    }
    
    .sidebar-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(229, 9, 20, 0.1), transparent);
        animation: shimmer 3s infinite;
    }
    
    @keyframes shimmer {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .sidebar-title {
        color: #ffffff;
        font-size: 2.2em;
        font-weight: 900;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        letter-spacing: 2px;
        position: relative;
        z-index: 2;
    }
    
    .sidebar-subtitle {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1em;
        margin: 8px 0 0 0;
        font-weight: 400;
        position: relative;
        z-index: 2;
    }
    
    /* Input Section Cards */
    .input-section {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 25px 20px;
        margin: 20px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    .input-section:hover {
        transform: translateY(-2px);
        border-color: rgba(229, 9, 20, 0.3);
        box-shadow: 0 8px 30px rgba(229, 9, 20, 0.1);
    }
    
    .section-icon {
        font-size: 1.5em;
        margin-right: 10px;
        color: #e50914;
    }
    
    .section-title {
        color: #ffffff;
        font-size: 1.3em;
        font-weight: 700;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding-bottom: 10px;
    }
    
    /* Enhanced Text Input Styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 2px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 15px !important;
        color: white !important;
        font-size: 16px !important;
        padding: 18px 25px !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        font-family: 'Inter', sans-serif !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
        width: 100% !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #e50914 !important;
        box-shadow: 0 0 0 4px rgba(229, 9, 20, 0.15) !important;
        background: rgba(255, 255, 255, 0.12) !important;
        transform: translateY(-2px);
        outline: none !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
        font-style: italic;
        font-weight: 400;
    }
    
    /* Enhanced SelectBox with Custom Styling */
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 2px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 15px !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: rgba(229, 9, 20, 0.4) !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 20px rgba(229, 9, 20, 0.15);
    }
    
    .stSelectbox > div > div > div {
        color: white !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 16px !important;
        padding: 15px 20px !important;
        background: transparent !important;
    }
    
    /* Enhanced Slider with Modern Design */
    .stSlider {
        margin: 25px 0 !important;
    }
    
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, rgba(229, 9, 20, 0.3) 0%, #e50914 100%) !important;
        height: 8px !important;
        border-radius: 15px !important;
        box-shadow: 0 2px 10px rgba(229, 9, 20, 0.3) !important;
    }
    
    .stSlider > div > div > div > div > div {
        background: linear-gradient(135deg, #ffffff 0%, #f0f0f0 100%) !important;
        border: 3px solid #e50914 !important;
        width: 24px !important;
        height: 24px !important;
        border-radius: 50% !important;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
    }
    
    .stSlider > div > div > div > div > div:hover {
        transform: scale(1.3);
        box-shadow: 0 6px 25px rgba(229, 9, 20, 0.6) !important;
        border-width: 4px !important;
    }
    
    /* Sidebar Labels with Icons */
    .stSidebar label {
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 600 !important;
        font-size: 15px !important;
        margin-bottom: 12px !important;
        font-family: 'Inter', sans-serif !important;
        display: block !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    
    /* Custom Number Input Display */
    .slider-value {
        background: linear-gradient(135deg, rgba(229, 9, 20, 0.2) 0%, rgba(229, 9, 20, 0.1) 100%);
        color: white;
        padding: 8px 15px;
        border-radius: 25px;
        font-weight: 600;
        text-align: center;
        margin-top: 10px;
        border: 1px solid rgba(229, 9, 20, 0.3);
        backdrop-filter: blur(10px);
        font-size: 14px;
    }
    
    /* Browse Collection Button Enhancement */
    .browse-button {
        background: linear-gradient(135deg, rgba(229, 9, 20, 0.15) 0%, rgba(229, 9, 20, 0.05) 100%) !important;
        border: 2px solid rgba(229, 9, 20, 0.3) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        margin: 25px 0 !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(15px) !important;
        cursor: pointer !important;
    }
    
    .browse-button:hover {
        background: linear-gradient(135deg, rgba(229, 9, 20, 0.25) 0%, rgba(229, 9, 20, 0.15) 100%) !important;
        border-color: rgba(229, 9, 20, 0.5) !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 10px 30px rgba(229, 9, 20, 0.2) !important;
    }
    
    .browse-icon {
        font-size: 2.5em;
        color: #e50914;
        margin-bottom: 10px;
        display: block;
    }
    
    .browse-title {
        color: white;
        font-size: 1.4em;
        font-weight: 700;
        margin-bottom: 8px;
    }
    
    .browse-subtitle {
        color: rgba(255, 255, 255, 0.7);
        font-size: 1em;
        font-weight: 400;
        line-height: 1.4;
    }
    
    /* Enhanced Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #e50914 0%, #b20710 100%);
        color: white;
        border: none;
        border-radius: 15px;
        padding: 18px 35px;
        font-weight: 700;
        font-size: 1.1em;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
        letter-spacing: 1.2px;
        box-shadow: 0 8px 25px rgba(229, 9, 20, 0.3);
        font-family: 'Inter', sans-serif;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
        border: 2px solid rgba(229, 9, 20, 0.5);
        width: 100%;
        margin: 15px 0;
    }
    
    .stButton > button:hover {
        transform: translateY(-4px) scale(1.03);
        box-shadow: 0 15px 40px rgba(229, 9, 20, 0.5);
        background: linear-gradient(135deg, #ff1e2d 0%, #e50914 100%);
        border-color: rgba(229, 9, 20, 0.8);
    }
    
    .stButton > button:active {
        transform: translateY(-1px) scale(1.01);
        box-shadow: 0 5px 20px rgba(229, 9, 20, 0.4);
    }
    
    /* Modern metric cards */
    .stMetric {
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(20px);
        padding: 25px 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    .stMetric:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3);
        border-color: rgba(229, 9, 20, 0.3);
    }
    
    /* Enhanced sidebar styling */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, rgba(229, 9, 20, 0.1) 0%, rgba(0, 0, 0, 0.95) 100%);
        backdrop-filter: blur(25px);
    }
    
    /* Modern alerts */
    .stAlert {
        border-radius: 20px;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }
    
    .stSuccess {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.2) 0%, rgba(139, 195, 74, 0.1) 100%);
        border-color: rgba(76, 175, 80, 0.3);
    }
    
    .stError {
        background: linear-gradient(135deg, rgba(244, 67, 54, 0.2) 0%, rgba(229, 57, 53, 0.1) 100%);
        border-color: rgba(244, 67, 54, 0.3);
    }
    
    .stWarning {
        background: linear-gradient(135deg, rgba(255, 193, 7, 0.2) 0%, rgba(255, 152, 0, 0.1) 100%);
        border-color: rgba(255, 193, 7, 0.3);
    }
    
    .stInfo {
        background: linear-gradient(135deg, rgba(33, 150, 243, 0.2) 0%, rgba(30, 136, 229, 0.1) 100%);
        border-color: rgba(33, 150, 243, 0.3);
    }
    
    /* Improved spinner */
    .stSpinner > div {
        border-color: #e50914 !important;
        border-top-color: transparent !important;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Enhanced container styling */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100%;
    }
    
    /* Modern scrollbar */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #e50914, #ff6b6b);
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #ff1e2d, #e50914);
        transform: scale(1.1);
    }
    
    /* Typography improvements */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Inter', 'Segoe UI', sans-serif;
        font-weight: 600;
        color: white;
    }
    
    p, span, div, label {
        font-family: 'Inter', 'Segoe UI', sans-serif;
        color: rgba(255, 255, 255, 0.9);
    }
    
    /* Download button styling */
    .stDownloadButton > button {
        background: linear-gradient(135deg, rgba(76, 175, 80, 0.8) 0%, rgba(139, 195, 74, 0.8) 100%);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 10px 20px;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(76, 175, 80, 0.4);
        background: linear-gradient(135deg, rgba(76, 175, 80, 1) 0%, rgba(139, 195, 74, 1) 100%);
    }
    
    /* Stylish recommendation button */
    .recommend-button {
        background: linear-gradient(135deg, #E50914 0%, #B20710 100%);
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 25px;
        font-size: 1.1em;
        font-weight: 600;
        cursor: pointer;
        width: 100%;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.3);
        margin: 20px 0;
    }
    .recommend-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(229, 9, 20, 0.4);
        background: linear-gradient(135deg, #F40612 0%, #C4070F 100%);
    }
</style>
""", unsafe_allow_html=True)

st.markdown(create_search_dropdown_netflix(), unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load data from CSV files with robust path resolution and fallback options"""
    
    # Define possible paths for CSV files
    possible_paths = [
        # Streamlit Cloud path (most likely)
        Path("/mount/src/recomender/recomender"),
        # Alternative Streamlit Cloud paths
        Path("/mount/src/recomender"),
        # Local development paths
        Path(__file__).parent.parent.parent / "recomender",
        Path("../../../recomender"),
        Path("../../recomender"),
        Path("./recomender"),
        Path("recomender"),
    ]
    
    # Try different file combinations (full dataset vs sample)
    file_combinations = [
        ("tmdb_5000_movies.csv", "tmdb_5000_credits.csv"),  # Full dataset
        ("sample_movies.csv", "sample_credits.csv"),        # Sample dataset
    ]
    
    for data_dir in possible_paths:
        for movies_file, credits_file in file_combinations:
            movies_csv = data_dir / movies_file
            credits_csv = data_dir / credits_file
            
            if movies_csv.exists() and credits_csv.exists():
                # Check if files are not empty
                try:
                    if movies_csv.stat().st_size > 1000 and credits_csv.stat().st_size > 1000:
                        if movies_file.startswith("sample"):
                            st.info(f"✅ Using sample dataset ({movies_file}, {credits_file})")
                        return str(movies_csv), str(credits_csv)
                except Exception:
                    continue
    
    # If no files found, show debug information
    st.error("🔍 **Debug Information - CSV Files Not Found**")
    st.write(f"**Current working directory:** `{Path.cwd()}`")
    st.write(f"**App file location:** `{Path(__file__).parent}`")
    
    # Check each path with detailed info
    st.write("**Checked these paths and files:**")
    for i, data_dir in enumerate(possible_paths, 1):
        st.write(f"{i}. `{data_dir}`")
        for movies_file, credits_file in file_combinations:
            movies_csv = data_dir / movies_file
            credits_csv = data_dir / credits_file
            st.write(f"   - {movies_file}: {movies_csv.exists()} | {credits_file}: {credits_csv.exists()}")
    
    # List all CSV files in the project
    st.write("**All CSV files found in the project:**")
    try:
        search_paths = [Path("/mount/src/recomender"), Path.cwd()]
        all_csv_files = []
        for search_path in search_paths:
            if search_path.exists():
                all_csv_files.extend(list(search_path.rglob("*.csv")))
        
        if all_csv_files:
            for file in all_csv_files:
                file_size = file.stat().st_size if file.exists() else 0
                st.write(f"  - `{file}` ({file_size:,} bytes)")
        else:
            st.write("  - No CSV files found")
    except Exception as e:
        st.write(f"  - Error listing files: {e}")
    
    return None, None

@st.cache_resource
def initialize_recommender():
    """Initialize the movie recommender system"""
    try:
        recommender = MovieRecommender()
        movies_path, credits_path = load_data()
        
        if movies_path and credits_path:
            # Show progress in Streamlit
            progress_container = st.empty()
            with progress_container.container():
                st.info("🔄 Initializing movie recommender system...")
                
                # Capture the output from the recommender
                import io
                import sys
                from contextlib import redirect_stdout, redirect_stderr
                
                # Create string buffers to capture output
                stdout_buffer = io.StringIO()
                stderr_buffer = io.StringIO()
                
                success = False
                with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
                    success = recommender.load_and_process_data(movies_path, credits_path)
                
                # Get the captured output
                stdout_output = stdout_buffer.getvalue()
                stderr_output = stderr_buffer.getvalue()
                
                # Show the debug output in Streamlit
                if stdout_output:
                    st.write("**Debug Output:**")
                    st.code(stdout_output, language="text")
                
                if stderr_output:
                    st.write("**Error Output:**")
                    st.code(stderr_output, language="text")
                
                if success:
                    progress_container.empty()
                    return recommender, None
                else:
                    return None, f"Failed to process movie data. Debug info shown above."
        else:
            return None, "Could not find CSV files in recomender folder"
    except Exception as e:
        st.error(f"Exception in initialize_recommender: {str(e)}")
        import traceback
        st.code(traceback.format_exc(), language="text")
        return None, f"Error: {str(e)}"

def display_movie_recommendations(recommendations, selected_movie):
    """Display movie recommendations in a clean grid layout"""
    if not recommendations:
        st.info("🎬 Select a movie to get personalized recommendations!")
        return
    
    st.markdown("---")
    st.markdown(f"### 🎯 Top {len(recommendations)} Recommendations for '{selected_movie}'")
    
    # Create grid layout for recommendations
    cols = st.columns(2)
    
    for idx, rec in enumerate(recommendations):
        col = cols[idx % 2]
        
        with col:
            # Use the cleaned up movie card component
            movie_card_html = create_movie_card_netflix(
                rec['title'], 
                rec['similarity_score'], 
                is_selected=False
            )
            st.markdown(movie_card_html, unsafe_allow_html=True)
    
    # Add download functionality
    st.markdown("---")
    recommendations_df = pd.DataFrame(recommendations)
    csv = recommendations_df.to_csv(index=False)
    
    st.download_button(
        label="📥 Download Recommendations as CSV",
        data=csv,
        file_name=f"recommendations_for_{selected_movie.replace(' ', '_')}.csv",
        mime="text/csv"
    )

def display_selected_movie(movie_title):
    """Display the selected movie with enhanced styling"""
    st.markdown("---")
    st.markdown("### 🎬 Selected Movie")
    
    # Create selected movie card
    selected_card_html = create_movie_card_netflix(
        movie_title, 
        similarity_score=None, 
        is_selected=True
    )
    
    # Center the selected movie card
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(selected_card_html, unsafe_allow_html=True)

def main():
    # Create header
    st.markdown(create_netflix_header(), unsafe_allow_html=True)
    
    # Initialize recommender
    recommender, error = initialize_recommender()
    
    if error:
        st.error(f"❌ {error}")
        st.info("Make sure tmdb_5000_movies.csv and tmdb_5000_credits.csv are in the recomender folder")
        return
    
    if not recommender:
        st.error("❌ Failed to initialize the movie recommender system")
        return
    
    # Get all movie titles
    all_movies = recommender.get_all_movie_titles()
    
    if not all_movies:
        st.error("❌ No movies found in the database")
        return
    
    st.success(f"✅ Loaded {len(all_movies)} movies successfully!")
    
    # Sidebar for movie selection
    st.sidebar.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(229, 9, 20, 0.2) 0%, rgba(229, 9, 20, 0.08) 100%);
        padding: 25px 20px;
        border-radius: 20px;
        border: 2px solid rgba(229, 9, 20, 0.3);
        box-shadow: 0 8px 25px rgba(229, 9, 20, 0.15);
        backdrop-filter: blur(20px);
        margin-bottom: 30px;
        text-align: center;
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(229, 9, 20, 0.1) 0%, transparent 70%);
            animation: pulse 3s ease-in-out infinite;
        "></div>
        <div style="position: relative; z-index: 2;">
            <h2 style="
                color: #ffffff;
                font-size: 1.9em;
                margin: 0 0 8px 0;
                font-weight: 700;
                letter-spacing: 1.5px;
                text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
                background: linear-gradient(135deg, #ffffff 0%, #ffcccc 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            ">🎯 Select a Movie</h2>
            <p style="
                color: rgba(255, 255, 255, 0.85);
                margin: 0;
                font-size: 0.95em;
                font-style: italic;
                font-weight: 400;
                letter-spacing: 0.5px;
            ">Discover your next favorite film</p>
        </div>
    </div>
    
    <style>
    @keyframes pulse {
        0%, 100% { opacity: 0.3; transform: scale(1); }
        50% { opacity: 0.6; transform: scale(1.05); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Search functionality with enhanced styling
    st.sidebar.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin-bottom: 25px;
        backdrop-filter: blur(15px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    ">
        <h4 style="
            color: #ffffff;
            font-size: 1.15em;
            margin: 0 0 15px 0;
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 600;
            letter-spacing: 0.8px;
        ">
            <span style="
                background: linear-gradient(135deg, #e50914, #ff6b6b);
                padding: 6px 8px;
                border-radius: 50%;
                font-size: 0.9em;
            ">🔍</span>
            Search Movies
        </h4>
        <p style="
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9em;
            margin: 0 0 15px 0;
            line-height: 1.4;
        ">Type to find your favorite movies quickly</p>
    </div>
    """, unsafe_allow_html=True)
    
    search_query = st.sidebar.text_input(
        "",
        placeholder="🎬 Type movie name here...",
        key="movie_search",
        help="Start typing to search through our movie database",
        label_visibility="collapsed"
    )
    
    # Browse section with improved styling
    st.sidebar.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        margin: 25px 0;
        backdrop-filter: blur(15px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    ">
        <h4 style="
            color: #ffffff;
            font-size: 1.15em;
            margin: 0 0 15px 0;
            display: flex;
            align-items: center;
            gap: 10px;
            font-weight: 600;
            letter-spacing: 0.8px;
        ">
            <span style="
                background: linear-gradient(135deg, #e50914, #ff6b6b);
                padding: 6px 8px;
                border-radius: 50%;
                font-size: 0.9em;
            ">🎬</span>
            Browse Collection
        </h4>
        <p style="
            color: rgba(255, 255, 255, 0.7);
            font-size: 0.9em;
            margin: 0 0 15px 0;
            line-height: 1.4;
        ">Explore our entire movie database</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filter movies based on search query
    if search_query:
        filtered_movies = [movie for movie in all_movies if search_query.lower() in movie.lower()]
        if filtered_movies:
            selected_movie = st.sidebar.selectbox(
                "",
                options=filtered_movies,
                key="filtered_movie_select",
                help=f"Found {len(filtered_movies)} movies matching your search"
            )
        else:
            st.sidebar.warning("🔍 No movies found matching your search. Try a different term.")
            selected_movie = st.sidebar.selectbox(
                "",
                options=all_movies,
                key="all_movies_fallback"
            )
    else:
        selected_movie = st.sidebar.selectbox(
            "",
            options=all_movies,
            key="movie_select",
            help="Browse through our collection of movies"
        )
    
    # Enhanced recommendations slider section
    st.sidebar.markdown("<div style='margin: 30px 0 20px 0;'></div>", unsafe_allow_html=True)
    
    st.sidebar.markdown("""
    <div style="
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 25px;
    ">
        <h4 style="
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.1em;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 8px;
        ">
            ⚙️ Number of recommendations:
        </h4>
    </div>
    """, unsafe_allow_html=True)
    
    num_recommendations = st.sidebar.slider(
        "",
        min_value=1,
        max_value=10,
        value=5,
        help="Choose how many movie recommendations you'd like to see"
    )
    
    # Add a stylish divider
    st.sidebar.markdown("""
    <div style="
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(229, 9, 20, 0.6), transparent);
        margin: 30px 0;
        border-radius: 2px;
    "></div>
    """, unsafe_allow_html=True)
    
    # Display statistics
    create_stats_cards_netflix(len(all_movies), selected_movie, 0)
    
    if selected_movie:
        # Selected movie section
        display_selected_movie(selected_movie)
        
        # Stylish recommendation button
        st.sidebar.markdown("""
        <style>
        .recommend-button {
            background: linear-gradient(135deg, #E50914 0%, #B20710 100%);
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 25px;
            font-size: 1.1em;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(229, 9, 20, 0.3);
            margin: 20px 0;
        }
        .recommend-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(229, 9, 20, 0.4);
            background: linear-gradient(135deg, #F40612 0%, #C4070F 100%);
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Center the button and add some spacing
        st.sidebar.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
        
        if st.sidebar.button("🎬 Get Recommendations", key="recommend_btn", use_container_width=True):
            st.session_state.show_recommendations = True
        
        # Add footer to sidebar
        st.sidebar.markdown("""
        <div style="
            margin-top: 50px;
            padding: 15px;
            text-align: center;
            color: rgba(255, 255, 255, 0.6);
            font-size: 0.9em;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        ">
            🎭 Discover your next favorite movie!
        </div>
        """, unsafe_allow_html=True)
    
        # Get recommendations button
        if st.button("✨ Get AI Recommendations", type="primary"):
            with st.spinner("Getting recommendations..."):
                recommendations = recommender.get_recommendations(selected_movie, num_recommendations)
            
            if recommendations:
                display_movie_recommendations(recommendations, selected_movie)
            else:
                st.warning("😔 No recommendations found for this movie.")
    
    else:
        # Welcome section
        st.markdown(create_featured_section(), unsafe_allow_html=True)
        
        # Show some example movies
        st.markdown("### 🎭 Featured Movies")
        example_movies = np.random.choice(all_movies, min(6, len(all_movies)), replace=False)
        
        cols = st.columns(3)
        for i, movie in enumerate(example_movies):
            with cols[i % 3]:
                st.markdown(create_movie_card_netflix(movie), unsafe_allow_html=True)



if __name__ == "__main__":
    main()
