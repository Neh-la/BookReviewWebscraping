Goodreads 100 Best Books Web Scraper
This project contains a Python script that uses Selenium to scrape the "100 Best Books of All Time" list from Goodreads. The script extracts book titles, authors, and ratings and saves the data in a CSV file.

Features
Scrapes book titles, authors, and ratings.
Saves data to a CSV file (goodreads_100_best_books.csv).
Uses Selenium for browser automation.
Requirements
Python Version
Python 3.7 or higher
Libraries
Install the required Python libraries using pip:

bash
Copy code
pip install selenium pandas
WebDriver
ChromeDriver: Ensure you have Google Chrome installed and download the corresponding ChromeDriver version.
Setup and Usage
1. Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/BookReviewWebscraping.git
cd BookReviewWebscraping
2. Set Up ChromeDriver
Download the correct version of ChromeDriver for your Chrome browser.
Place the chromedriver.exe file in the appropriate directory.
Update the driver_path variable in the script with the correct file path:
python
Copy code
driver_path = r"C:\path\to\chromedriver.exe"
3. Run the Script
Run the script to scrape the data:

bash
Copy code
python goodreads_scraper.py
4. Output
The scraped data will be saved in a CSV file named goodreads_100_best_books.csv in the same directory.
Repository Structure
graphql
Copy code
BookReviewWebscraping/
├── goodreads_scraper.py   # The main Python script
├── README.md              # Project documentation
└── goodreads_100_best_books.csv  # Generated CSV file after scraping
Troubleshooting
WebDriverException: Message: chromedriver not found

Ensure ChromeDriver is installed and the path is set correctly.
Add the ChromeDriver directory to your system's PATH.
Empty Output

Check your internet connection.
Ensure the Goodreads webpage structure has not changed.
