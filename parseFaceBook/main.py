import time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests


def login(url):
    driver = webdriver.Firefox()
    driver.get(url)
    PHONE = "+380971585620"
    PASSWORD = "sosok2021"
    time.sleep(2)
    driver.find_element("id", "email").send_keys(PHONE)
    driver.find_element("id", "pass").send_keys(PASSWORD)
    driver.find_element("id", "loginbutton").click()
    time.sleep(7)
    get_post(driver)
    time.sleep(5)


def get_post(driver):
    SCROLL_PAUSE_TIME = 2
    k = 0
    while k < 200:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        k += 1
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    feed = soup.find("div", role="feed")
    soup = BeautifulSoup(str(feed), "html.parser")
    img = soup.find_all("img", alt="Возможно, это изображение 1 человек")
    k = 0
    for i in img:
        k += 1
        download_image(i['src'], k)


def download_image(img, k):
    try:
        response = requests.get(img)
        img = response.content
        with open(f'pictures/photo{k}.png', 'wb') as handler:
            handler.write(img)
    except:
        return


def main():
    url = 'https://www.facebook.com/groups/501372487206777'
    login(url)


main()
