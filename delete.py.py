#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.common.by import By

# Define the URL of the Audible search page
website = "https://www.audible.com/search"

# Create a Chrome WebDriver instance
driver = webdriver.Chrome()

# Navigate to the Audible website
driver.get(website)

# Define the container that holds the list of books
container = driver.find_element(By.CLASS_NAME, "adbl-impression-container")

# Initialize lists to store scraped data
book_title_list = []
book_author_list = []
book_length_list = []

try:
    # Find the pagination element
    pagination = driver.find_element(By.XPATH, '//ul[contains(@class,"pagingElements")]')
    pages = pagination.find_elements(By.TAG_NAME, "bc-list-item")

    # Check if there are pages
    if len(pages) > 0:
        last_page = int(pages[-1].text)  # Get the last page number

        # Loop through the pages
        for current_page in range(1, last_page + 1):
            print(f"Scraping page {current_page}...")

            # Find and scrape book titles, authors, and lengths
            book_titles = driver.find_elements(By.CLASS_NAME, "bc-pub-break-word")
            book_authors = driver.find_elements(By.CLASS_NAME, "authorLabel")
            book_lengths = driver.find_elements(By.CLASS_NAME, "runtimeLabel")

            # Iterate through the elements and add them to the respective lists
            for title, author, length in zip(book_titles, book_authors, book_lengths):
                book_title_list.append(title.text)
                book_author_list.append(author.text[3:])
                book_length_list.append(length.text[7:])

            # Click on the next page button
            if current_page < last_page:
                button_to_next_page = driver.find_element(By.XPATH, "your_next_page_button_xpath_here")
                button_to_next_page.click()

    else:
        print("No pagination found on the page.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the WebDriver
driver.quit()

