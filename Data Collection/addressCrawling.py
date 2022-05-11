from ast import keyword
from lib2to3.pgen2 import driver
from webbrowser import Chrome
import pandas as pd
import time
# df = pd.read_csv('sample_shop_info_missdata.csv', sep=',', encoding='UTF-8')
# df['addressmix']=df['name']+""+df['misaddress']  

# from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')

# for i, keyword in enumerate(df['name'].tolist()):
#     print(keyword, end='')
#     try:
#         kakao_map_search_url=f"https://map.kakao.com/?q={keyword}"
#         driver.get(kakao_map_search_url)
#         time.sleep(1)
#         addresFind = driver.find_element_by_css_selector("#info\.search\.place\.list > li:nth-child(1) > div.info_item > div.addr > p:nth-child(1)").text
       
#         print("address" + addresFind)
         
#     except Exception as e1:
#         print("정보 없음")
#         pass 
#