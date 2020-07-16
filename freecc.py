import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time

page_num = 1
    
def scrape_one():
    global page_num
    result = requests.get(f'https://f1.lv/2020/page/{page_num}/')
    src = result.content
    soup = BeautifulSoup(src, 'lxml')

    div_part = soup.select('div.td_module_1.td_module_wrap.td-animation-stack > h3')
    print(f'Sraping page nr {page_num}.')
    page_num += 1

    # # exports csv
    # for link in div_part:
    #     with open('item.csv', 'a+') as f:
    #         fixed_text = link.text.replace(",", "-")
    #         f.write(fixed_text + ',')
    #         f.write(link.a.get('href') + '\n')

    # exports json
    for link in div_part:
        with open('item.json', 'a+') as f:
            fixed_text = link.text.replace(",", "-")
            f.write(f'"Name": "{fixed_text}",\n')
            f.write(f'"Url": "{link.a.get("href")}",\n')
            # f.write(link.a.get('href') + '\n')


while page_num < 31:
    time.sleep(2)
    scrape_one()