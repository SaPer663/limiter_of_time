import requests
import time
import logging
from bs4 import BeautifulSoup
from consts import auth_form, auth_headers, auth_url_post, dhcp_list_url, dhcp_list_headers, continue_url
from consts import deny_form, deny_headers, disable_form, disable_headers, url_deny_disable, continue_headers
from consts import wireless_url, wireless_headers, mac_address, deny_homedevice_form, deny_all_form
from data_extraction import to_separate_mac_address, data_extraction_from_html

# authorization -----------------------------------------

def authorization():
    r = requests.post(auth_url_post, headers=auth_headers, data=auth_form)
    if r.status_code == 200:
        print('access')
    else:
        print(r.status_code)
# continue 'button'  come back at network filter menu  
def get_continue():
    r = requests.get(continue_url, headers=continue_headers)
    if r.status_code == 200:
        print('continue')
    else:
        print(r.status_code)


# deny_post ------------------------------------------Lena_access_off
def mac_filter_on():
    authorization()
    logger = logging.getLogger("is_mac.requests_to.filter_on")
    logger.info("mac_filter_on")
    r = requests.get(dhcp_list_url, headers=dhcp_list_headers) 
    if r.status_code == 200:
        dhcp_list = data_extraction_from_html(r.text, 'dhcp_list') # получение списка девайсов подкл. к роут.
        deny_form['dhcp_list'] = dhcp_list   # изменнение списка в форме запроса
    else:
        return print(r.status_code)
    if False: # проверка вкл. ли фильтр
        print('already_Deny')
    else:
        r = requests.post(url_deny_disable, headers=deny_headers, data=deny_form)
        if r.status_code == 200:
            time.sleep(15)
            print('DENY')
            get_continue()
        else:
            print(r.status_code)

#off homedevice and Lena
def mac_filter_on_for_all():
    authorization()
    logger = logging.getLogger("is_mac.requests_to.filter_on")
    logger.info("mac_filter_on")
    r = requests.get(dhcp_list_url, headers=dhcp_list_headers) 
    if r.status_code == 200:
        dhcp_list = data_extraction_from_html(r.text, 'dhcp_list') # получение списка девайсов подкл. к роут.
        deny_form['dhcp_list'] = dhcp_list   # изменнение списка в форме запроса
    else:
        return print(r.status_code)
    if False: # проверка вкл. ли фильтр
        print('already_Deny')
    else:
        r = requests.post(url_deny_disable, headers=deny_headers, data=deny_all_form)
        if r.status_code == 200:
            time.sleep(15)
            print('DENY')
            get_continue()
        else:
            print(r.status_code)
    
#off homedevice
def mac_filter_on_for_homedevice():
    authorization()
    logger = logging.getLogger("is_mac.requests_to.filter_on")
    logger.info("mac_filter_on")
    r = requests.get(dhcp_list_url, headers=dhcp_list_headers) 
    if r.status_code == 200:
        dhcp_list = data_extraction_from_html(r.text, 'dhcp_list') # получение списка девайсов подкл. к роут.
        deny_homedevice_form['dhcp_list'] = dhcp_list   # изменнение списка в форме запроса
        print(dhcp_list)
    else:
        return print(r.status_code)
    if False: # проверка вкл. ли фильтр
        print('already_Deny')
    else:
        r = requests.post(url_deny_disable, headers=deny_headers, data=deny_homedevice_form)
        if r.status_code == 200:
            time.sleep(15)
            print('DENY')
            get_continue()
        else:
            print(r.status_code)


# disable_post --------------------------
def mac_filter_off():
    authorization()
    logger = logging.getLogger("is_mac.requests_to.filter_off")
    logger.info("mac_filter_off")
    r = requests.get(dhcp_list_url, headers=dhcp_list_headers)
    if r.status_code == 200:
        dhcp_list = data_extraction_from_html(r.text, 'dhcp_list')
        deny_form['dhcp_list'] = dhcp_list
    else:
        return print(r.status_code)
    time.sleep(5)
    if True:
        time.sleep(5)
        r = requests.post(url_deny_disable, headers=disable_headers, data=disable_form)
        if r.status_code == 200:
            time.sleep(15)
            print('DISABLE')
            get_continue()
        else:
            print(r.status_code)
    else:
        print('already_disable')    
# todo сделать проверку статуса мак_фильтра

# check mac in wirelist
def check_mac(mac_address):
    authorization()
    logger = logging.getLogger("is_mac.requests_to.check_mac")
    logger.info("check_mac")
    r = requests.get(wireless_url, headers=wireless_headers)
    if r.status_code == 200:
        if mac_address in to_separate_mac_address(mac_address):
            return True
        else:
            return False
    else:
        return False
