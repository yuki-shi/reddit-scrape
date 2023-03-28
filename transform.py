# Importing necessary libraries
from bs4 import BeautifulSoup
import pandas as pd
import os.path

def transform_to_dataframe(page_source):
  """
  This function takes in the page source of a Reddit page and extracts relevant information from it to create a pandas dataframe.
  
  Args:
  page_source (str): The HTML source code of the Reddit page.
  
  Returns:
  pandas.DataFrame: A dataframe containing information about the posts on the Reddit page.
  """
  
  # Parsing the HTML source code using BeautifulSoup
  soup = BeautifulSoup(page_source, 'html.parser')
  
  # Finding all the divs with id 'siteTable'
  pages = soup.find_all('div', {'id':'siteTable'})

  # Creating an empty list to store the information about each post
  posts = []

  # Looping through each page and each post on the page to extract relevant information
  for page in pages:
    for entry in page.find_all('div', {'class': 'top-matter'}):
      posts.append([f"https://www.reddit.com{entry.find('a', {'class': 'title'})['href']}", # URL of the post
                    entry.find('a', {'class': 'title'}).text, # Title of the post
                    entry.find('time').get('title'), # Time the post was submitted
                    entry.find('a', {'class':'author'}).text if entry.find('a', {'class':'author'}) else '[deleted]', # Username of the post author
                    ])

  # Creating a pandas dataframe from the list of posts
  df = pd.DataFrame(posts, columns=['url', 'title', 'posted', 'user'])
  
  # Saving the dataframe as a CSV file
  df.to_csv('reddit_data.csv', index=False)

  # Printing the absolute path of the saved CSV file
  print(f'.csv salvo em {os.path.abspath("reddit_data.csv")}')
  
  # Returning the dataframe
  return df