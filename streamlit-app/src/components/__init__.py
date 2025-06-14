import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_netflix_header():
    """Create a modern header with glassmorphism and animated gradient"""
    return """
    <div style="
        background: linear-gradient(135deg, rgba(15, 15, 35, 0.95) 0%, rgba(26, 13, 26, 0.9) 50%, rgba(13, 17, 23, 0.95) 100%);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        padding: 30px 40px;
        margin: -1rem -1rem 2rem -1rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 80%, rgba(229, 9, 20, 0.15) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 107, 107, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 40%, rgba(75, 0, 130, 0.1) 0%, transparent 50%);
            animation: backgroundShift 8s ease-in-out infinite;
        "></div>
        <div style="position: relative; z-index: 2;">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 15px;">
                <div style="display: flex; align-items: center;">
                    <h1 style="
                        margin: 0; 
                        font-size: 3.5em; 
                        font-weight: 900; 
                        background: linear-gradient(135deg, #e50914 0%, #ff6b6b 50%, #ff8e53 100%);
                        -webkit-background-clip: text;
                        -webkit-text-fill-color: transparent;
                        background-clip: text;
                        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
                        text-shadow: 0 0 30px rgba(229, 9, 20, 0.3);
                        letter-spacing: -3px;
                        animation: glow 3s ease-in-out infinite alternate;
                    ">MOVIEFLIX</h1>
                    <div style="
                        margin-left: 25px;
                        background: linear-gradient(135deg, rgba(229, 9, 20, 0.2) 0%, rgba(255, 107, 107, 0.1) 100%);
                        backdrop-filter: blur(15px);
                        border: 1px solid rgba(229, 9, 20, 0.4);
                        padding: 10px 18px;
                        border-radius: 30px;
                        font-size: 0.85em;
                        font-weight: 700;
                        color: #ff6b6b;
                        text-transform: uppercase;
                        letter-spacing: 2px;
                        animation: pulse 2.5s infinite;
                        box-shadow: 0 4px 15px rgba(229, 9, 20, 0.2);
                    ">🤖 AI Powered</div>
                </div>
                <div style="
                    color: rgba(255, 255, 255, 0.8);
                    font-size: 1.2em;
                    font-weight: 300;
                    font-family: 'Segoe UI', sans-serif;
                    opacity: 0.9;
                ">
                    🎬 Discover • Explore • Enjoy
                </div>
            </div>
            <p style="
                margin: 0; 
                font-size: 1.3em; 
                color: rgba(255, 255, 255, 0.85);
                font-weight: 300;
                max-width: 800px;
                line-height: 1.7;
                font-family: 'Segoe UI', sans-serif;
            ">
                Your personal AI movie curator powered by advanced machine learning algorithms
            </p>
        </div>
        <style>
            @keyframes backgroundShift {
                0%, 100% { opacity: 1; }
                33% { opacity: 0.8; }
                66% { opacity: 0.9; }
            }
            @keyframes glow {
                0% { text-shadow: 0 0 30px rgba(229, 9, 20, 0.3); }
                100% { text-shadow: 0 0 40px rgba(229, 9, 20, 0.6), 0 0 60px rgba(255, 107, 107, 0.3); }
            }
            @keyframes pulse {
                0%, 100% { 
                    opacity: 1; 
                    transform: scale(1); 
                    box-shadow: 0 4px 15px rgba(229, 9, 20, 0.2);
                }
                50% { 
                    opacity: 0.9; 
                    transform: scale(1.05); 
                    box-shadow: 0 6px 20px rgba(229, 9, 20, 0.4);
                }
            }
        </style>
    </div>
    """

def create_movie_card_netflix(title, similarity_score=None, is_selected=False):
    """Create a simple movie card with just the movie name"""
    # Clean the title of any HTML entities or special characters
    clean_title = str(title).strip()
    
    # Determine styling based on selection
    if is_selected:
        border_color = "#e50914"
        bg_color = "rgba(229, 9, 20, 0.2)"
    else:
        border_color = "rgba(255, 255, 255, 0.3)"
        bg_color = "rgba(255, 255, 255, 0.1)"
    
    # Format similarity score
    score_text = f"{similarity_score:.0%} Match" if similarity_score else ""
    
    return f"""
    <div style="
        background: {bg_color};
        border: 2px solid {border_color};
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        text-align: center;
        color: white;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
    ">
        <h3 style="
            margin: 0;
            color: white;
            font-size: 1.2em;
            font-weight: 600;
        ">{clean_title}</h3>
        {f'<p style="color: #ff6b6b; margin: 10px 0 0 0; font-size: 0.9em;">{score_text}</p>' if score_text else ''}
    </div>
    """

def create_search_dropdown_netflix():
    """Modern search and input styling with glassmorphism"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border: 2px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 25px !important;
        color: white !important;
        padding: 18px 28px !important;
        font-size: 1.1em !important;
        font-family: 'Inter', 'Segoe UI', sans-serif !important;
        font-weight: 400 !important;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: rgba(229, 9, 20, 0.8) !important;
        box-shadow: 0 0 30px rgba(229, 9, 20, 0.3), 0 4px 25px rgba(0, 0, 0, 0.2) !important;
        transform: translateY(-2px) scale(1.02) !important;
        background: rgba(255, 255, 255, 0.12) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
        font-style: italic !important;
        font-weight: 300 !important;
    }
    
    .stSelectbox > div > div > div {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px) !important;
        border: 2px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 20px !important;
        color: white !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
    }
    
    .stSelectbox > div > div > div:hover {
        border-color: rgba(229, 9, 20, 0.5) !important;
        box-shadow: 0 0 20px rgba(229, 9, 20, 0.2) !important;
        transform: translateY(-1px) !important;
    }
    
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #e50914, #ff6b6b) !important;
        height: 6px !important;
        border-radius: 3px !important;
    }
    
    .stSlider > div > div > div > div > div {
        background: white !important;
        border: 3px solid #e50914 !important;
        box-shadow: 0 0 10px rgba(229, 9, 20, 0.3) !important;
    }
    
    .stRadio > div {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 20px !important;
        padding: 20px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        transition: all 0.3s ease !important;
    }
    
    .stRadio > div:hover {
        border-color: rgba(229, 9, 20, 0.3) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }
    </style>
    """

def create_stats_cards_netflix(total_movies, selected_movie=None, recommendations_count=0):
    """Create clean statistics cards using Streamlit's native components"""
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🎬 Movies Available",
            value=f"{total_movies:,}",
            help="Total movies in our database"
        )
    
    with col2:
        st.metric(
            label="🤖 AI Engine", 
            value="Active",
            help="Machine learning recommendation system"
        )
    
    with col3:
        selection_status = "Selected" if selected_movie else "None"
        st.metric(
            label="🎭 Current Selection",
            value=selection_status,
            help="Movie you've chosen for recommendations"
        )
    
    with col4:
        st.metric(
            label="🎯 Recommendations",
            value=str(recommendations_count),
            help="Number of movie recommendations generated"
        )

def create_recommendation_chart_netflix(recommendations):
    """Create a modern chart with glassmorphism styling"""
    if not recommendations:
        return None
    
    titles = [rec['title'][:20] + '...' if len(rec['title']) > 20 else rec['title'] for rec in recommendations]
    scores = [rec['similarity_score'] for rec in recommendations]
    
    fig = go.Figure(data=[
        go.Bar(
            x=titles,
            y=scores,
            marker=dict(
                color=scores,
                colorscale=[[0, '#e50914'], [0.5, '#ff6b6b'], [1, '#ff8e53']],
                line=dict(color='rgba(255,255,255,0.2)', width=1)
            ),
            hovertemplate='<b>%{x}</b><br>Similarity: %{y:.1%}<extra></extra>',
            texttemplate='%{y:.0%}',
            textposition='outside'
        )
    ])
    
    fig.update_layout(
        title=dict(
            text="🎯 Recommendation Similarity Scores",
            font=dict(size=20, color='white', family='Inter, Segoe UI'),
            x=0.5
        ),
        xaxis=dict(
            title="Movies",
            titlefont=dict(color='rgba(255,255,255,0.8)', size=14),
            tickfont=dict(color='rgba(255,255,255,0.7)', size=12),
            gridcolor='rgba(255,255,255,0.1)',
            showgrid=True
        ),
        yaxis=dict(
            title="Similarity Score",
            titlefont=dict(color='rgba(255,255,255,0.8)', size=14),
            tickfont=dict(color='rgba(255,255,255,0.7)', size=12),
            gridcolor='rgba(255,255,255,0.1)',
            showgrid=True,
            tickformat='.0%'
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', family='Inter, Segoe UI'),
        showlegend=False,
        margin=dict(t=60, b=60, l=60, r=60),
        height=400
    )
    
    return fig

def create_featured_section():
    """Create a modern featured section with advanced styling"""
    return """
    <div style="
        background: linear-gradient(135deg, rgba(229, 9, 20, 0.15) 0%, rgba(0, 0, 0, 0.4) 100%);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border-radius: 30px;
        padding: 40px;
        margin: 30px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    ">
        <div style="
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 30% 70%, rgba(229, 9, 20, 0.1) 0%, transparent 60%),
                radial-gradient(circle at 70% 30%, rgba(255, 107, 107, 0.08) 0%, transparent 60%);
            pointer-events: none;
        "></div>
        <div style="position: relative; z-index: 2;">
            <div style="text-align: center; margin-bottom: 40px;">
                <h2 style="
                    color: white;
                    font-size: 2.8em;
                    margin: 0 0 15px 0;
                    font-weight: 700;
                    font-family: 'Inter', 'Segoe UI', sans-serif;
                    background: linear-gradient(135deg, #ffffff 0%, #ff6b6b 100%);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    background-clip: text;
                ">🌟 How MovieFlix AI Works</h2>
                <p style="
                    color: rgba(255, 255, 255, 0.8); 
                    font-size: 1.2em; 
                    margin: 0;
                    font-family: 'Segoe UI', sans-serif;
                    font-weight: 300;
                ">
                    Discover your perfect movie match using advanced machine learning
                </p>
            </div>
            <div style="
                display: grid; 
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
                gap: 30px; 
                margin-top: 30px;
            ">
                <div style="
                    background: rgba(255, 255, 255, 0.08);
                    backdrop-filter: blur(15px);
                    padding: 30px;
                    border-radius: 25px;
                    border: 1px solid rgba(229, 9, 20, 0.3);
                    border-left: 4px solid #e50914;
                    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                    cursor: pointer;
                " onmouseover="
                    this.style.transform = 'translateY(-8px) scale(1.02)'; 
                    this.style.boxShadow = '0 15px 40px rgba(229, 9, 20, 0.2)';
                    this.style.borderColor = 'rgba(229, 9, 20, 0.6)';
                " onmouseout="
                    this.style.transform = 'translateY(0) scale(1)'; 
                    this.style.boxShadow = 'none';
                    this.style.borderColor = 'rgba(229, 9, 20, 0.3)';
                ">
                    <div style="font-size: 3em; margin-bottom: 20px; text-align: center;">🔍</div>
                    <h4 style="
                        color: #e50914; 
                        margin: 0 0 15px 0; 
                        font-size: 1.4em; 
                        font-family: 'Inter', 'Segoe UI', sans-serif;
                        font-weight: 600;
                    ">Intelligent Search</h4>
                    <p style="
                        color: rgba(255, 255, 255, 0.85); 
                        margin: 0; 
                        line-height: 1.7; 
                        font-family: 'Segoe UI', sans-serif;
                        font-size: 1.05em;
                    ">
                        Our smart search instantly finds movies from our vast database with real-time suggestions and fuzzy matching capabilities.
                    </p>
                </div>
                <div style="
                    background: rgba(255, 255, 255, 0.08);
                    backdrop-filter: blur(15px);
                    padding: 30px;
                    border-radius: 25px;
                    border: 1px solid rgba(255, 107, 107, 0.3);
                    border-left: 4px solid #ff6b6b;
                    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                    cursor: pointer;
                " onmouseover="
                    this.style.transform = 'translateY(-8px) scale(1.02)'; 
                    this.style.boxShadow = '0 15px 40px rgba(255, 107, 107, 0.2)';
                    this.style.borderColor = 'rgba(255, 107, 107, 0.6)';
                " onmouseout="
                    this.style.transform = 'translateY(0) scale(1)'; 
                    this.style.boxShadow = 'none';
                    this.style.borderColor = 'rgba(255, 107, 107, 0.3)';
                ">
                    <div style="font-size: 3em; margin-bottom: 20px; text-align: center;">🤖</div>
                    <h4 style="
                        color: #ff6b6b; 
                        margin: 0 0 15px 0; 
                        font-size: 1.4em; 
                        font-family: 'Inter', 'Segoe UI', sans-serif;
                        font-weight: 600;
                    ">AI Analysis Engine</h4>
                    <p style="
                        color: rgba(255, 255, 255, 0.85); 
                        margin: 0; 
                        line-height: 1.7; 
                        font-family: 'Segoe UI', sans-serif;
                        font-size: 1.05em;
                    ">
                        Advanced machine learning analyzes genres, cast, directors, and plot summaries using TF-IDF vectorization and cosine similarity.
                    </p>
                </div>
                <div style="
                    background: rgba(255, 255, 255, 0.08);
                    backdrop-filter: blur(15px);
                    padding: 30px;
                    border-radius: 25px;
                    border: 1px solid rgba(248, 181, 0, 0.3);
                    border-left: 4px solid #f8b500;
                    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                    cursor: pointer;
                " onmouseover="
                    this.style.transform = 'translateY(-8px) scale(1.02)'; 
                    this.style.boxShadow = '0 15px 40px rgba(248, 181, 0, 0.2)';
                    this.style.borderColor = 'rgba(248, 181, 0, 0.6)';
                " onmouseout="
                    this.style.transform = 'translateY(0) scale(1)'; 
                    this.style.boxShadow = 'none';
                    this.style.borderColor = 'rgba(248, 181, 0, 0.3)';
                ">
                    <div style="font-size: 3em; margin-bottom: 20px; text-align: center;">🎯</div>
                    <h4 style="
                        color: #f8b500; 
                        margin: 0 0 15px 0; 
                        font-size: 1.4em; 
                        font-family: 'Inter', 'Segoe UI', sans-serif;
                        font-weight: 600;
                    ">Perfect Matches</h4>
                    <p style="
                        color: rgba(255, 255, 255, 0.85); 
                        margin: 0; 
                        line-height: 1.7; 
                        font-family: 'Segoe UI', sans-serif;
                        font-size: 1.05em;
                    ">
                        Get personalized recommendations with detailed similarity scores and discover your next favorite movie with confidence.
                    </p>
                </div>
            </div>
        </div>
    </div>
    """