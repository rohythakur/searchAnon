import os

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType



proxy_address = "127.0.0.1:8118"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,

})

tor = '/home/logic/Documents/tor-browser_en-US/Browser/firefox'
firefox_binary = FirefoxBinary(tor)





def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)



infoDirectory = 'data'
create_dir(infoDirectory)
