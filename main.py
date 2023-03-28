# Importing necessary modules
from transform import transform_to_dataframe
from reddit import Reddit

# Defining the main function
def main():
  # Setting the path for the Chrome driver
  driver_path = '/usr/bin/chromedriver'
  
  # Creating an instance of the Reddit class
  reddit = Reddit(driver_path)
  
  # Setting the URL to scrape
  url = 'https://old.reddit.com/r/copypastabr/new/'
  
  # Setting the initial date for the data to be scraped
  data_inicial = '2023/02/28' # %Y/%m/%d
  
  # Extracting the page source using the Reddit class method
  page_source = reddit.extract_page_source(url, data_inicial)
  
  # Transforming the page source into a pandas dataframe using the transform module
  transform_to_dataframe(page_source)

# Running the main function if the script is being run directly
if __name__ == '__main__':
  main()