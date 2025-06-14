import pandas as pd
import numpy as np
import re

# Try to import scikit-learn with better error handling
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError as e:
    print(f"Warning: scikit-learn not available ({e}). Using basic recommendation fallback.")
    SKLEARN_AVAILABLE = False
    
    # Create a basic fallback recommendation system
    class TfidfVectorizer:
        def __init__(self, *args, **kwargs):
            self.vocabulary = {}
        
        def fit_transform(self, texts):
            # Simple word frequency approach as fallback
            import re
            from collections import Counter
            
            # Build vocabulary from all texts
            all_words = []
            for text in texts:
                words = re.findall(r'\b\w+\b', str(text).lower())
                all_words.extend(words)
            
            # Get top 1000 most common words
            word_counts = Counter(all_words)
            top_words = [word for word, count in word_counts.most_common(1000)]
            self.vocabulary = {word: i for i, word in enumerate(top_words)}
            
            # Create simple term frequency matrix
            matrix = []
            for text in texts:
                words = re.findall(r'\b\w+\b', str(text).lower())
                word_counts = Counter(words)
                vector = [word_counts.get(word, 0) for word in top_words]
                matrix.append(vector)
            
            return np.array(matrix)
    
    def cosine_similarity(matrix):
        # Simple cosine similarity implementation
        if matrix.shape[0] == 0:
            return np.array([[]])
        
        # Normalize the matrix
        norms = np.sqrt(np.sum(matrix * matrix, axis=1))
        norms[norms == 0] = 1  # Avoid division by zero
        normalized = matrix / norms[:, np.newaxis]
        
        # Compute cosine similarity
        return np.dot(normalized, normalized.T)

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
            print(f"Loading movies from: {movies_path}")
            self.movies_df = pd.read_csv(movies_path)
            print(f"Loaded {len(self.movies_df)} movies")
            
            print(f"Loading credits from: {credits_path}")
            self.credits_df = pd.read_csv(credits_path)
            print(f"Loaded {len(self.credits_df)} credits")
            
            # Check if we have the required columns
            required_movie_cols = ['title', 'overview', 'genres', 'keywords']
            required_credit_cols = ['title', 'cast', 'crew']
            
            missing_movie_cols = [col for col in required_movie_cols if col not in self.movies_df.columns]
            missing_credit_cols = [col for col in required_credit_cols if col not in self.credits_df.columns]
            
            if missing_movie_cols:
                print(f"Missing required movie columns: {missing_movie_cols}")
                return False
            if missing_credit_cols:
                print(f"Missing required credit columns: {missing_credit_cols}")
                return False
            
            # Merge the dataframes on title (inner join to keep only matching titles)
            print("Merging dataframes...")
            merged_df = self.movies_df.merge(self.credits_df, on='title', how='inner')
            print(f"After merge: {len(merged_df)} movies with complete data")
            
            if len(merged_df) == 0:
                print("No movies found after merging. Using movies data without credits.")
                # Fallback: use movies data without credits
                self.movies_df = self.movies_df.copy()
                self.movies_df['cast'] = ''
                self.movies_df['crew'] = ''
            else:
                self.movies_df = merged_df
            
            # Keep only necessary columns and handle missing data
            available_features = []
            for feature in ['title', 'overview', 'genres', 'keywords', 'cast', 'crew']:
                if feature in self.movies_df.columns:
                    available_features.append(feature)
            
            self.movies_df = self.movies_df[available_features].copy()
            
            # Fill missing values
            for col in ['overview', 'genres', 'keywords', 'cast', 'crew']:
                if col in self.movies_df.columns:
                    self.movies_df[col] = self.movies_df[col].fillna('')
            
            # Remove rows with empty titles
            self.movies_df = self.movies_df[self.movies_df['title'].notna() & (self.movies_df['title'] != '')]
            
            print(f"Final dataset: {len(self.movies_df)} movies")
            
            if len(self.movies_df) == 0:
                print("No valid movies remaining after processing")
                return False
            
            # Create combined features
            feature_columns = [col for col in ['overview', 'genres', 'keywords', 'cast', 'crew'] 
                             if col in self.movies_df.columns]
            
            self.movies_df['combined_features'] = ''
            for col in feature_columns:
                self.movies_df['combined_features'] += ' ' + self.movies_df[col].astype(str)
            
            # Clean and process the text
            self.movies_df['combined_features'] = self.movies_df['combined_features'].apply(self._clean_text)
            
            # Create TF-IDF matrix
            if SKLEARN_AVAILABLE:
                print("Creating TF-IDF matrix with scikit-learn...")
            else:
                print("Creating TF-IDF matrix with fallback implementation...")
            
            tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
            tfidf_matrix = tfidf.fit_transform(self.movies_df['combined_features'])
            
            # Calculate cosine similarity
            print("Calculating similarity matrix...")
            self.similarity_matrix = cosine_similarity(tfidf_matrix)
            
            # Get movie titles
            self.movie_titles = self.movies_df['title'].tolist()
            
            if SKLEARN_AVAILABLE:
                print(f"✅ Successfully processed {len(self.movie_titles)} movies with scikit-learn")
            else:
                print(f"✅ Successfully processed {len(self.movie_titles)} movies with fallback system")
            
            return True
            
        except Exception as e:
            print(f"Error processing data: {e}")
            import traceback
            traceback.print_exc()
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