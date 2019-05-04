import requests

url = 'http://192.168.0.1'
url_post = 'http://192.168.0.1/login.cgi'

headers = { 'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding' : 'gzip, deflate',
'Accept-Language' : 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Connection' : 'keep-alive',
'Content-Length' : '154',                             #post 
'Content-Type' : 'application/x-www-form-urlencoded', #post
'Host' : '192.168.0.1',
'Referer' : 'http://192.168.0.1/login_auth.asp',      #post
'Upgrade-Insecure-Requests' : '1',
'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0' }

form = {'html_response_page' : 'login_fail.asp',
'login_name' : 'YWRtaW4A',
'login_pass' : 'NzJBR19TYVBlcg==',
'graph_id' : '7a3db',
'log_pass' : 'NzJBR19TYVBlcg==',
'graph_code' : '',	
'login' : 'Login'}

#r = requests.get(url, headers = headers)
r = requests.post(url_post, headers=headers, data=form)
if r.status_code == 200:
    print('OK')
else:
    print(r.status_code)
print(r.text)
r = requests.get('http://192.168.0.1/st_wireless.asp', headers=headers)
if r.status_code == 200:
    print(r.text)
<input type="hidden" id="wireless_station_list" name="wireless_station_list" 
'''value="
00:e1:b0:10:da:12/33/802.11g/ /52M/192.168.0.5,
78:24:af:62:42:63/31/802.11n/ /65M/192.168.0.4,
3c:cb:7c:89:59:8e/50/802.11n/ /65M/192.168.0.3,
e0:ca:94:36:30:74/55/802.11n/ /65M/192.168.0.6,">
'''