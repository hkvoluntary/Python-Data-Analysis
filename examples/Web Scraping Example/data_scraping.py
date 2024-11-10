import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page with the data table
url = "https://www.usinflationcalculator.com/inflation/consumer-price-index-and-annual-percent-changes-from-1913-to-2008/"

# Send a GET request to the page
response = requests.get(url, verify=False)


def cleaning_data(data_list, header, cleaned_data, missed_data):
    header_length = len(header)
    for row in data_list:
        if (len(row) == header_length):
            cleaned_data.append(row)  # Append to good data
        else:
            missed_data.append(row)  # Append to missed data

# Check if the request was successful
if response.status_code == 200:
   #Parse the page content
   soup = BeautifulSoup(response.text, 'html.parser')
      # Checkpoint - make sure we got the data
   #print(soup.prettify())
   # Find the table with from URL. Use "view page source"
   table = soup.find('table')
   # Checkpoint - see the data
   #print(table)

   # Review the header and the data items. Some page are using tag <th> 
   # For this page, it uses tag <tr> as well. 
   
   # Extract table rows
   rows = table.find_all('tr')

   # Create list to store the data
   data_list = []
   for row in rows:
      cells = row.find_all('td')
      if len(cells) > 0:
         row_data = [cell.text.strip() for cell in cells]
         # checkpoint 
         #print(row_data)
         data_list.append(row_data)
   # Data clearing
   # Review the data, we can drop the first row and second row is header
   header = data_list[1]
   data_list = data_list[2:]
   # Data clearing
   # Make sure the number of row items is matched to header. Then it is ok to transform to dataframe
   cleaned_data = []
   missed_data = []
   cleaning_data(data_list, header, cleaned_data, missed_data)
   # Check point
   print(cleaned_data)
   print(missed_data)
   # Need to make the decision what about the missed data
   df = pd.DataFrame(cleaned_data, columns=header) 
   # Check point
   print(df)
   df.to_csv('./cpi_data.csv', index=False)
else:
   print(f"Failed to retrieve the page. Status code: {response.status_code}")
