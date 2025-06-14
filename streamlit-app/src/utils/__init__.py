import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

class MovieRecommender:
    def __init__(self):
        self.movies_df = None
        self.credits_df = None
        self.similarity_matrix = None
        self.movie_titles = []
        
    def load_and_process_data(self, movies_path, credits_path):
        """Load and process the movie data"""
        try:
            # Load the data
            self.movies_df = pd.read_csv(movies_path)
            self.credits_df = pd.read_csv(credits_path)
            
            # Merge the dataframes
            self.movies_df = self.movies_df.merge(self.credits_df, on='title')
            
            # Keep only necessary columns
            features = ['title', 'overview', 'genres', 'keywords', 'cast', 'crew']
            self.movies_df = self.movies_df[features].dropna()
            
            # Create combined features
            self.movies_df['combined_features'] = (
                self.movies_df['overview'].fillna('') + ' ' +
                self.movies_df['genres'].fillna('') + ' ' +
                self.movies_df['keywords'].fillna('') + ' ' +
                self.movies_df['cast'].fillna('') + ' ' +
                self.movies_df['crew'].fillna('')
            )
            
            # Clean and process the text
            self.movies_df['combined_features'] = self.movies_df['combined_features'].apply(self._clean_text)
            
            # Create TF-IDF matrix
            tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
            tfidf_matrix = tfidf.fit_transform(self.movies_df['combined_features'])
            
            # Calculate cosine similarity
            self.similarity_matrix = cosine_similarity(tfidf_matrix)
            
            # Get movie titles
            self.movie_titles = self.movies_df['title'].tolist()
            
            return True
            
        except Exception as e:
            print(f"Error processing data: {e}")
            return False
    
    def _clean_text(self, text):
        """Clean and preprocess text"""
        # Remove special characters and convert to lowercase
        text = re.sub(r'[^a-zA-Z\s]', '', str(text).lower())
        return text
    
    def get_all_movie_titles(self):
        """Get all movie titles"""
        return self.movie_titles if self.movie_titles else []
    
    def get_recommendations(self, movie_title, num_recommendations=5):
        """Get movie recommendations"""
        try:
            if movie_title not in self.movie_titles:
                return []
            
            # Get the index of the movie
            movie_index = self.movie_titles.index(movie_title)
            
            # Get similarity scores for this movie
            similarity_scores = list(enumerate(self.similarity_matrix[movie_index]))
            
            # Sort by similarity score (excluding the movie itself)
            similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:]
            
            # Get top recommendations
            recommendations = []
            for i in range(min(num_recommendations, len(similarity_scores))):
                idx = similarity_scores[i][0]
                recommendations.append({
                    'title': self.movie_titles[idx],
                    'similarity_score': similarity_scores[i][1]
                })
            
            return recommendations
            
        except Exception as e:
            print(f"Error getting recommendations: {e}")
            return []

def some_utility_function():
    pass

def another_utility_function():
    pass

__all__ = ['MovieRecommender', 'some_utility_function', 'another_utility_function']