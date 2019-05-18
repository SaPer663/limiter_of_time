import re
from bs4 import BeautifulSoup

def data_extraction_from_html(html_doc, id): 
    soup = BeautifulSoup(html_doc, features='lxml')
    try:
        return soup.find(attrs={'id': id})['value']
    except TypeError:
        return None

def to_separate_mac_address(string): # парсим список мак_адресов с веб-морды роутера
    pattern = r'[0-9a-fA-F]{2}(?:[:-][0-9a-fA-F]{2}){5}' 
    return re.findall(pattern, string)
