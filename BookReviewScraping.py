from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Set up the Selenium WebDriver
driver_path = r"C:\Users\nehla\MovieReviewScraping\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Replace with your path to ChromeDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# URL of Goodreads list for "100 Best Books of All Time"
url = 'https://www.goodreads.com/list/show/9440.100_Best_Books_of_All_Time_The_World_Library_List'
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Extract book titles, authors, and ratings
books = driver.find_elements(By.CSS_SELECTOR, 'a.bookTitle')
authors = driver.find_elements(By.CSS_SELECTOR, 'a.authorName')
ratings = driver.find_elements(By.CSS_SELECTOR, 'span.minirating')

# Create an empty list to store book information
book_list = []

# Loop through the data and collect book details
for i in range(len(books)):
    try:
        title = books[i].text.strip()
        author = authors[i].text.strip()
        rating = ratings[i].text.strip()
        
        book_data = {
            "Title": title,
            "Author": author,
            "Rating": rating
        }
        book_list.append(book_data)
        
        # Print the book details
        print(f"{i + 1}. Title: {title}, Author: {author}, Rating: {rating}")
    except IndexError:
        # Handle cases where some information might be missing
        continue

# Convert the list to a DataFrame and save as CSV
df = pd.DataFrame(book_list)
df.to_csv('goodreads_100_best_books.csv', index=False)

print("\nScraping completed. Data saved to 'goodreads_100_best_books.csv'")

# Close the browser
driver.quit()
