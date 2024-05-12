import time
from bs4 import BeautifulSoup
from selenium import webdriver
import json


def get_links(start_link):
    driver = webdriver.Firefox()
    driver.get(start_link)
    time.sleep(10)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    page_number = int(soup.find_all("a", class_="page-link")[-2].text)
    links = []
    for i in range(15, page_number + 1):
        driver.get(f"https://wanted.mvs.gov.ua/searchbezvesti?page={i}")
        html_content_link = driver.page_source
        soup_link = BeautifulSoup(html_content_link, 'html.parser')
        page_links = soup_link.find_all("a", class_="card padding-none")
        for link in page_links:
            links.append(link['href'])
            page_link = "https://wanted.mvs.gov.ua" + link['href']
            get_info(page_link)


def get_info(link):
    driver = webdriver.Firefox()
    driver.get(link)
    time.sleep(10)
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    data = soup.find_all("div", class_="default-text small")
    try:
        department = data[0].text
    except:
        department = None
        print("department" + link)
    try:
        status = data[1].text
    except:
        status = None
        print("status" + link)
    try:
        disappearance_date = data[2].text
    except:
        disappearance_date = None
        print("disappearance_date" + link)
    try:
        disappearance_place = data[3].text
    except:
        disappearance_place = None
        print("disappearance_place" + link)
    try:
        surname = data[4].text
    except:
        surname = None
        print("surname" + link)
    try:
        name = data[5].text
    except:
        name = None
        print("name" + link)
    try:
        father_name = data[6].text
    except:
        father_name = None
        print("father_name" + link)
    try:
        surname_rus = data[7].text
    except:
        surname_rus = None
        print("surname_rus" + link)
    try:
        name_rus = data[8].text
    except:
        name_rus = None
        print("name_rus" + link)
    try:
        father_name_rus = data[9].text
    except:
        father_name_rus = None
        print("father_name_rus" + link)
    try:
        date_of_birth = data[10].text
    except:
        date_of_birth = None
        print("date_of_birth" + link)
    try:
        gender = data[11].text
    except:
        gender = None
        print("gender" + link)
    try:
        description = data[12].text
    except:
        description = None
        print("description" + link)
    try:
        special_data = data[13].text
    except:
        special_data = None
        print("special_data" + link)
    try:
        contact_data = data[14].text
    except:
        contact_data = None
        print("contact_data" + link)
    try:
        image = soup.find("img", class_="card-img")['src']
    except:
        image = None
        print("image" + link)
    driver.close()
    data = {
        "disappearance_date": disappearance_date,
        "disappearance_place": disappearance_place,
        "surname": surname,
        "name": name,
        "father_name": father_name,
        "surname_rus": surname_rus,
        "name_rus": name_rus,
        "father_name_rus": father_name_rus,
        "date_of_birth": date_of_birth,
        "gender": gender,
        "description": description,
        "special_data": special_data,
        "contact_data": contact_data,
        "image": image
    }
    write_to_json(data)


def write_to_json(data):
    with open("job.json", "a", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.write(",")


def main():
    get_links("https://wanted.mvs.gov.ua/searchbezvesti/")


main()
