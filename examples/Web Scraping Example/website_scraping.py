# Credit to https://charlieojackson.co.uk/python/python-web-crawler.php
import sqlite3
import time
import requests  # HTTP client library
from bs4 import BeautifulSoup  # package for parsing HTML and XML documents

# Set the timer
start = time.time()

# Variable
all_urls = [] # List to store URLs
link_counter = 0 # Counter for the while loop
URL = ""
db_table_name = "websites"

# User provides the URL for crawling
URL = input("URL to crawl: ")
if len(URL) < 1:
    URL = "https://charlieojackson.co.uk"

all_urls.append(URL) # Append the start URL in the List

# connect to database
db = sqlite3.connect('./site_crawl.db')
cursor = db.cursor()

# Table schema
# "ID" INTEGER - PRIMARY KEY AUTOINCREMENT
# "Title" varchar(255)
# "Description" varchar(255)
# "Number_of_links" INTEGER
# "Contents" TEXT
# "Time" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# 'IF NOT EXISTS' clause means new domains will create a new table
create_table_sql = "CREATE TABLE IF NOT EXISTS " + db_table_name + \
   "(ID INTEGER PRIMARY KEY AUTOINCREMENT,URL varchar(255)," + \
   "Title varchar(255),Description varchar(255),Number_of_links " + \
   "INTEGER,Contents TEXT, Time TIMESTAMP DEFAULT " + \
   "CURRENT_TIMESTAMP)"

# Create table 
cursor.execute(create_table_sql)


# Inserting data into SQLite database
def insert_data(extracted_data):
   page_url, page_title, page_description, page_contents, page_total_links = extracted_data
   cursor.execute(
      "INSERT INTO " + db_table_name + " (URL, Title, Description, Number_of_links, Contents) VALUES(?,?,?,?,?)",
      (page_url, page_title, page_description, page_total_links, page_contents))
   db.commit()

# Extracting page information
def extract_content(page_soup):
   # Extract required data for crawled page
   page_title = page_soup.title.string
   try:
      page_description = page_soup.find("meta", {"name": "description"})['content']
   except:
      page_description = "NULL"

   page_contents_raw = page_soup.text  # Plain text only
   page_contents = page_contents_raw.replace("\n", "")  # Remove the newlines
   return page_title, page_description, page_contents

# Find all the links with the method 'find_all('a')' passing in 'a' as a parameter.
# Loop through the links and run a couple conditionals
def extract_links(page_soup):
   # Extract links and link counts from page
   page_links_raw = soup.find_all('a')
   for link in page_links_raw:
      # Look for the valid URLs with same domain and append it to the list if it is not there yet.
      if str(link.get('href')).startswith(URL) == True and link.get('href') not in all_urls:
      # Skip if it is jpg and png images link
         if '.jpg' in link.get('href') or '.png' in link.get('href'):
            continue
         else:
            # Append the link to our list
            all_urls.append(link.get('href'))
   pass
   # total number of links found on the page.
   total_count = len(page_links_raw)
   return total_count

# This loop runs until the counter is bigger than the length of the list i.e. there are no more URL's to crawl.
while link_counter < len(all_urls):

   try:
      print("Loop Counter: %d - Crawling: %s " % (link_counter, all_urls[link_counter]))
      r = requests.get(all_urls[link_counter])
      if r.status_code == 200:
         html = r.text
         soup = BeautifulSoup(html, "html.parser")
         # View page source
         #print(soup.prettify())
         # Getting total links count
         no_of_links = extract_links(soup)
         # Getting title, description, page contents
         title, description, contents = extract_content(soup)
         print("Page title: %s \n"
               "Page description: %s \n"
               "Page contents: %s \n"
               "Total links count: %d \n" % (title, description, contents, no_of_links))
         # Insert the crawled data into the database
         insert_data((all_urls[link_counter], title, description, contents, no_of_links))
         link_counter += 1  # increment to stop the while loop
      else:
         break

   except Exception as err:  # Error handling
      link_counter += 1  # increment to stop the while loop
      print(str(err))

# Close the table and database
cursor.close()
db.close()
# Find the total crawling time
end = time.time()
print("Total crawling time: ", end - start)
