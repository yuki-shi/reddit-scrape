from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import datetime as dt

class Reddit():
  def __init__(self, driver_path):
    self.driver_path = driver_path
    self.driver = self.init_driver()

  def init_driver(self):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")
    return webdriver.Chrome(options=options, executable_path=self.driver_path)

  def extract_page_source(self, url, data_limite):
    self.driver.get(url)
    self.driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/button[2]').click()

    data_limite = (dt.datetime.strptime(data_limite, '%Y/%m/%d'))#.strftime('%b %d')

    pages = []
    data_final = dt.datetime.now()
    #re_pattern = r'(?<= {1}).{3} [0-9]+(?= )'

    while data_final > data_limite:
      pages.extend(self.driver.page_source)
      dates = [x.get_attribute('title') for x in self.driver.find_elements(By.TAG_NAME, 'time')]
      data_final = (dt.datetime.strptime(dates[-1], '%a %b %d %H:%M:%S %Y %Z'))#.strftime('%b %d')
      self.driver.find_element(By.XPATH, '//a[contains(text(), "próximo")]').click()

    self.driver.quit()

    print('Extração completa!')

    #with open('source.html', 'w') as f:
    #  for page in pages:
    #    f.write(page)

    return ''.join(pages) # tornamos a lista uma str para preparar para o BeautifulSoup