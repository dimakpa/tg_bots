from selenium import webdriver
from pages import HomePage
#https://github.com/mozilla/geckodriver/releases
browser = webdriver.Chrome("C:/Users/dimak/Desktop/Learning/Project/Cod/chromdriver.exe")
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
f = open('login.txt', 'r')
login = f.read()
f.close()

fp = open('password.txt', 'r')
password = fp.read()
fp.close()

login_page.login(login, password)

browser.close()