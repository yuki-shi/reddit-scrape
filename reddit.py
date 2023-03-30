# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime as dt

class Reddit():
  def __init__(self, driver_path: str):
    """
    Initializes the Reddit class with the driver path.

    Args:
    driver_path (str): The path of the webdriver.

    Returns:
    None
    """
    self.driver_path = driver_path
    self.driver = self.init_driver()

  def init_driver(self):
    """
    Initializes the webdriver with the specified options.

    Args:
    None

    Returns:
    webdriver.Chrome: The initialized webdriver.
    """
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    return webdriver.Chrome(options=options, executable_path=self.driver_path)

  def extract_page_source(self, url: str, data_limite: str) -> str:
    """
    Extracts the page source of the given url until the specified date.

    Args:
    url (str): The url of the page to extract.
    data_limite (str): The date until which to extract the page source in the format 'YYYY/MM/DD'.

    Returns:
    str: The concatenated page source of all the pages extracted.
    """
    self.driver.get(url)
    
    # TODO: this only happens on subreddits tagged as +18, add an exception
    self.driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/button[2]').click()

    # Converting end date to datetime object 
    data_limite = (dt.datetime.strptime(data_limite, '%Y/%m/%d'))#.strftime('%b %d')

    # Creating an empty list to store the source code of each page
    pages = []
    
    # Creating a dummy value for the iteration
    data_final = dt.datetime.now()

    # Browse and extract each page until the last post's date matches the desired end date
    while data_final > data_limite:
      pages.extend(self.driver.page_source)
      dates = [x.get_attribute('title') for x in self.driver.find_elements(By.TAG_NAME, 'time')]
      data_final = (dt.datetime.strptime(dates[-1], '%a %b %d %H:%M:%S %Y %Z'))#.strftime('%b %d')
      self.driver.find_element(By.XPATH, '//a[contains(text(), "próximo")]').click()

    self.driver.quit()

    print('Extração completa!')

  # Converting list to a concatenated string for BeautifulSoup
    return ''.join(pages) 
