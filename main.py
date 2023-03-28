from transform import transform_to_dataframe
from reddit import Reddit

def main():
  driver_path = '/usr/bin/chromedriver'
  reddit = Reddit(driver_path)
  url = 'https://old.reddit.com/r/copypastabr/new/'
  data_inicial = '2023/02/28' # %Y/%m/%d
  page_source = reddit.extract_page_source(url, data_inicial)
  transform_to_dataframe(page_source)

if __name__ == '__main__':
  main()