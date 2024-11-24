# Book Review Scraping Project

A Python-based web scraping project that collects and analyzes book reviews from Goodreads, specifically focusing on the "100 Best Books of All Time" list.

## Project Overview

This project aims to:
- Scrape book information from Goodreads' "100 Best Books of All Time" list
- Extract book titles, authors, and ratings
- Generate insightful visualizations for data analysis
- Store the collected data in a structured format

## Features

### Data Collection
- Automated web scraping using Selenium
- Extraction of book titles, authors, and ratings
- Data storage in CSV format

### Data Visualization
- Rating distribution analysis
- Top-rated books visualization
- Author analysis (authors with multiple books)
- Ratings vs. Popularity correlation analysis

## Requirements

- Python 3.x
- Chrome WebDriver
- Required packages:
  - selenium==4.18.1
  - webdriver-manager==4.0.1
  - pandas==2.1.1
  - numpy==1.24.3
  - matplotlib==3.8.0
  - seaborn==0.12.2
  - beautifulsoup4==4.12.2
  - requests==2.31.0
  - lxml==4.9.3
  - python-dotenv==1.0.0

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Ensure you have Chrome browser installed
5. Update the Chrome WebDriver path in `BookReviewScraping.py` if necessary

## Usage

1. Run the scraper:
   ```
   python BookReviewScraping.py
   ```
   This will collect book data and save it to `goodreads_100_best_books.csv`

2. Generate visualizations:
   ```
   python visualizations.py
   ```
   This will create four visualization files:
   - `rating_distribution.png`: Distribution of book ratings
   - `top_rated_books.png`: Top 10 highest-rated books
   - `author_analysis.png`: Authors with multiple books in the list
   - `ratings_vs_popularity.png`: Correlation between ratings and popularity

## Project Structure

```
BookReviewScraping/
├── README.md
├── requirements.txt
├── BookReviewScraping.py    # Web scraping script
├── visualizations.py        # Data visualization script
├── goodreads_100_best_books.csv    # Scraped data
└── *.png                    # Generated visualization files
```

## Output

The project generates several visualization files that provide insights into the book data:
- Rating distribution across all books
- Horizontal bar chart of the highest-rated books
- Analysis of authors with multiple books in the top 100
- Scatter plot showing the relationship between ratings and number of ratings

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
