from bs4 import BeautifulSoup

def data_extraction_from_html(html_doc, id):
    soup = BeautifulSoup(html_doc, features='lxml')
    try:
        return soup.find(attrs={'id': id})['value']
    except TypeError:
        return None

def isDeny(html_doc):
    if data_extraction_from_html(html_doc, 'mac_filter_00') != None:
        return True
    else:
        return False
        
