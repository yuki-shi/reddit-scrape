from bs4 import BeautifulSoup
import pandas as pd
import os.path

def transform_to_dataframe(page_source):
  #with open('./source.html') as f:
  #  soup = BeautifulSoup(f, 'html.parser')

  soup = BeautifulSoup(page_source, 'html.parser')
  pages = soup.find_all('div', {'id':'siteTable'})

  posts = []

  for page in pages:

    for entry in page.find_all('div', {'class': 'top-matter'}):
      posts.append([f"https://www.reddit.com{entry.find('a', {'class': 'title'})['href']}",
                    entry.find('a', {'class': 'title'}).text,
                    entry.find('time').get('title'),
                    entry.find('a', {'class':'author'}).text if entry.find('a', {'class':'author'}) else '[deleted]',
                    ])

  df = pd.DataFrame(posts, columns=['url', 'title', 'posted', 'user'])
  df.to_csv('reddit_data.csv', index=False)

  print(f'.csv salvo em {os.path.abspath("reddit_data.csv")}')
  return