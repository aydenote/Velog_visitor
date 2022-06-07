from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
browser = webdriver.Chrome('./chromedriver')
browser.implicitly_wait(3)


# 자동 로그인 url
browser.get('https://github.com/login?client_id=7c3902d881910d52ae3e&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id%3D7c3902d881910d52ae3e%26redirect_uri%3Dhttps%253A%252F%252Fv2.velog.io%252Fapi%252Fv2%252Fauth%252Fsocial%252Fcallback%252Fgithub%253Fnext%253D%252F%2540aydenote%26scope%3Duser%253Aemail')
browser.find_element_by_name('login').send_keys('GIT_USER_ID')
browser.find_element_by_name('password').send_keys('GIT_USER_PW')
browser.find_element_by_name('commit').click()

browser.implicitly_wait(4)

# 각 포스팅 경로 url
path = []
for i in range(1, 21):
    path.append(f'#root>div:nth-child(2)>div:nth-child(3)>div:nth-child(4)>div:nth-child(3)>div:first-child>div:nth-child({i})>a:nth-child(2)')

total=0

browser.implicitly_wait(4)
# 포스팅별 통계 클릭
for val in path:
    browser.get("https://velog.io/@aydenote")
    browser.find_element_by_css_selector(val).click()
    browser.find_element_by_xpath('//*[@id="root"]/div[2]/div[3]/div/div[1]/button[1]').click()
    total+= int(browser.find_element_by_css_selector('#root>div:nth-child(2)>main>div>div:nth-child(1)>div:nth-child(1)>span:nth-child(2)').text)


print(total)

