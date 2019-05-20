from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

print('네이버 실시간 검색어 순위') 

driver = webdriver.Chrome(executable_path=r"C:/Users/candy/Desktop/NEXT/Django_search/chromedriver.exe")

drvier.get('https://www.naver.com/')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
rank = drvier.find_elements_by_css_selector('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li:nth-child(1) > a.ah_a > span.ah_k')

texts = [rank.text for rank in ranks]

print(texts)