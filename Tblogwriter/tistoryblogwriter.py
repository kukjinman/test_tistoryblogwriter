import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=opt)


def tistoryLogin():

    url = "https://www.tistory.com/auth/login"
    browser.get(url)
    time.sleep(0.5)


    kakaologinbtn = browser.find_element(By.CSS_SELECTOR, "a.btn_login.link_kakao_id span.txt_login")
    kakaologinbtn.click()

    id = browser.find_element(By.CSS_SELECTOR,"input#loginId--1")
    id.send_keys("thater@naver.com")
    passwd = browser.find_element(By.CSS_SELECTOR,"input#password--2")
    passwd.send_keys("zlfmdk1!14")

    loginbtn = browser.find_element(By.CSS_SELECTOR, "button.btn_g.highlight.submit")
    loginbtn.click()



def tistoryWriter():
    browser.get("https://kukjinman-bwriter.tistory.com/manage/post")

    # tistory의 팝업 처리 - 기존 글의 이어쓰기 팝업 처리 코드
    da = Alert(browser)
    da.dismiss()





def runtistoryBlogWriter():
    tistoryLogin()
    time.sleep(1.5)
    tistoryWriter()


runtistoryBlogWriter()
