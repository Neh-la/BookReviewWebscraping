import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np

class BookReviewVisualizer:
    def __init__(self, data_path):
        """
        Initialize the visualizer with the path to the book review data.
        
        Args:
            data_path (str): Path to the CSV file containing book review data
        """
        self.data_path = Path(data_path)
        self.df = None
        self.load_data()
        
    def load_data(self):
        """Load the book review data from CSV file and process ratings."""
        try:
            self.df = pd.read_csv(self.data_path)
            # Extract numeric rating from the rating string (e.g., "4.50 avg rating — 1,193,480 ratings")
            self.df['Rating_Numeric'] = self.df['Rating'].str.extract(r'(\d+\.\d+)').astype(float)
            # Extract number of ratings
            self.df['Number_of_Ratings'] = self.df['Rating'].str.extract(r'—\s*([\d,]+)').iloc[:, 0].str.replace(',', '').astype(float)
        except FileNotFoundError:
            print(f"Error: Data file not found at {self.data_path}")
            return
            
    def setup_plot_style(self):
        """Set up the general plotting style."""
        plt.style.use('seaborn')
        sns.set_palette("husl")
        
    def plot_rating_distribution(self, save_path=None):
        """Create a histogram of book ratings distribution."""
        if self.df is None:
            return
            
        plt.figure(figsize=(12, 6))
        sns.histplot(data=self.df, x='Rating_Numeric', bins=20)
        plt.title('Distribution of Book Ratings', fontsize=14)
        plt.xlabel('Rating', fontsize=12)
        plt.ylabel('Number of Books', fontsize=12)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        else:
            plt.show()
        plt.close()
        
    def plot_top_rated_books(self, n=10, save_path=None):
        """Create a horizontal bar plot of top n rated books."""
        if self.df is None:
            return
            
        top_books = self.df.nlargest(n, 'Rating_Numeric')
        
        plt.figure(figsize=(12, 8))
        bars = plt.barh(top_books['Title'], top_books['Rating_Numeric'])
        plt.title(f'Top {n} Highest Rated Books', fontsize=14)
        plt.xlabel('Rating', fontsize=12)
        
        # Rotate y-axis labels for better readability
        plt.yticks(fontsize=10)
        
        # Add value labels on the bars
        for i, bar in enumerate(bars):
            width = bar.get_width()
            plt.text(width, bar.get_y() + bar.get_height()/2,
                    f'{width:.2f}',
                    ha='left', va='center', fontsize=10)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        else:
            plt.show()
        plt.close()
        
    def plot_author_analysis(self, save_path=None):
        """Create a visualization showing authors with multiple books in the list."""
        if self.df is None:
            return
            
        author_counts = self.df['Author'].value_counts()
        authors_multiple_books = author_counts[author_counts > 1]
        
        if len(authors_multiple_books) > 0:
            plt.figure(figsize=(10, 6))
            sns.barplot(x=authors_multiple_books.values, y=authors_multiple_books.index)
            plt.title('Authors with Multiple Books in Top 100', fontsize=14)
            plt.xlabel('Number of Books', fontsize=12)
            plt.ylabel('Author', fontsize=12)
            
            if save_path:
                plt.savefig(save_path, bbox_inches='tight', dpi=300)
            else:
                plt.show()
            plt.close()
            
    def plot_ratings_vs_popularity(self, save_path=None):
        """Create a scatter plot showing relationship between ratings and number of ratings."""
        if self.df is None:
            return
            
        plt.figure(figsize=(12, 8))
        sns.scatterplot(data=self.df, x='Number_of_Ratings', y='Rating_Numeric', alpha=0.6)
        plt.title('Book Ratings vs. Popularity', fontsize=14)
        plt.xlabel('Number of Ratings (Popularity)', fontsize=12)
        plt.ylabel('Average Rating', fontsize=12)
        
        # Add trend line
        z = np.polyfit(self.df['Number_of_Ratings'], self.df['Rating_Numeric'], 1)
        p = np.poly1d(z)
        plt.plot(self.df['Number_of_Ratings'], p(self.df['Number_of_Ratings']), "r--", alpha=0.8)
        
        if save_path:
            plt.savefig(save_path, bbox_inches='tight', dpi=300)
        else:
            plt.show()
        plt.close()

def main():
    """Run the visualization analysis."""
    visualizer = BookReviewVisualizer('goodreads_100_best_books.csv')
    
    # Create visualizations
    visualizer.plot_rating_distribution('rating_distribution.png')
    visualizer.plot_top_rated_books(10, 'top_rated_books.png')
    visualizer.plot_author_analysis('author_analysis.png')
    visualizer.plot_ratings_vs_popularity('ratings_vs_popularity.png')
    
    print("Visualizations have been created and saved!")

if __name__ == "__main__":
    main()
