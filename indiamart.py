import pandas as pd
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
agent=UserAgent()
def scrap_amazon(product):
  url = "https://dir.indiamart.com/search.mp?ss=oxygen+purity+meter&prdsrc=1&src=as-rcnt%7Cpos%3D2%7Ccat%3D-2%7Cmcat%3D-2%7Ckwd_len%3D0%7Ckwd_cnt%3D0&res=RC3&qu=to"
  headers = {
            'authority': 'www.indiamart.com',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'user-agent':agent.random,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        }
  response=requests.get(url,headers=headers)
  #print(response.text)
  soup = BeautifulSoup(response.text , 'html.parser')
  #print(soup);
  product_info_elements = soup.find_all("a", class_="prd-name")
  product_price_elements = soup.find_all("span", class_="prc clr3 fwb fs18 cp")
  print(product_info_elements)
  product_name_details = []
  product_price_details = []
  '''for product_info_element in product_info_elements:
        product_name = product_info_element.text
        product_name_details.append(product_name)
  for product_price_element in product_price_elements:
    product_price = product_price_element.text
    product_price_details.append(product_price)
    max_length = max(len(product_name_details),len(product_price_details))
    df = pd.DataFrame({'Product_name          ': product_name_details + [None] * (max_length - len(product_name_details)), 'Product_price': product_price_details + [None] * (max_length - len(product_price_details))})
    excel_file_path = 'indiamart_data.xlsx'
    df.to_excel(excel_file_path, index=False)'''
scrap_amazon("")

