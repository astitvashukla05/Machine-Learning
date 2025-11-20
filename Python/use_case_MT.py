url1='https://docs.langchain.com/?_gl=1*c1qx3f*_gcl_au*MTgwMTc4MDQ2NC4xNzYzNTUwMTA5*_ga*MTgzODEwMDI3Ny4xNzYzNTUwMTEw*_ga_47WX3HKKY2*czE3NjM1NTAxMTAkbzEkZzAkdDE3NjM1NTAxMTAkajYwJGwwJGgw'
url2='https://academy.langchain.com/?_gl=1*ettcji*_gcl_au*MTgwMTc4MDQ2NC4xNzYzNTUwMTA5*_ga*MTgzODEwMDI3Ny4xNzYzNTUwMTEw*_ga_47WX3HKKY2*czE3NjM1NTAxMTAkbzEkZzEkdDE3NjM1NTAxNjUkajUkbDAkaDA.'
url3='https://academy.langchain.com/'

import threading 
import requests

from bs4 import BeautifulSoup

urls=[url1,url2,url3]

def fetch_contents(url):
    response=requests.get(url)
    soap=BeautifulSoup(response.content,'html.parser')
    print(soap.text)

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()