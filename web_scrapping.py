import requests
from bs4 import BeautifulSoup
import re
import fnmatch
import pandas as pd
from urllib3 import request

# from urllib3  import pa

# list of websites to extract company names
website = ['http://ppprocessingltd.co.uk', 'http://www.feredaycylinder.com'
    , 'https://alphalaser.de'
    , 'https://www.onealmfgservices.com'
    , 'https://www.taupitz.biz'
    , 'http://www.bolducleroux.ca'
    , 'https://www.ferricmachinery.com'
    , 'http://www.jfe-steel.co.jp'
    , 'https://mewi-metallform.de'
           ]

# Based on inspecting each website, some of the key words found after inspecting

pattern = ['GmbH', 'Ltd', 'Limited', 'Spa', 'Machinery', 'Corporation', 'Leroux', 'Group', 'Inc']
# list of tags
tags = ['p', 'a', 'l1', 'h1', 'font', 'li', 'ul']

# Soup & REGEX libraries used to extract company names

def scrap_company(site):
    # r site in website1:
    print("website = ", site)
    data = requests.get(site)
    websoup = BeautifulSoup(data.text, 'html.parser')
    for tg in tags:
        #         print('tag--> ',tg)
        for div in websoup.find_all(tg):
            raw_cmpny = div.text
            for ptn in pattern:

                #                 if fnmatch.fnmatch(raw_cmpny, '*' + ptn + '*'):
                #                     process_company = raw_cmpny.split(ptn)[0].strip()  # this will stip out pattern and also newline also whitespaces

                regx_expr = '.*' + ptn

                # '[\D|\s|\n|\t]*'+ptn #'[A-z|a-z|\s|\&|\n|\t]*'+ptn
                # print('>',raw_cmpny)

                if re.match(regx_expr, raw_cmpny):
                    process_company = re.findall(regx_expr, raw_cmpny)[0]
                    try:
                        print(site, ':', process_company[-50:])
                    except:
                        print(site, ':', process_company)


def main():
    print('list of websites are -->\n', str(website))
    company_name = str(input("key in the website from the list above:"))
    if not re.match('[http://|https://].*', company_name):
        try:
            company_name = 'http://' + company_name
        except:
            company_name = 'https://' + company_name
    scrap_company(company_name)

# main class
if __name__ == '__main__':
    main()



