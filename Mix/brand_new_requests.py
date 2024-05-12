import json
import time

import requests
import os

directory = "D:/Workspace/Mix/pictures"
url_create = "https://34.118.102.90:8443/api/v1/coincidences/"
url_post = "https://34.118.102.90:8443/api/v1/uploads/"
url_create_missing = 'https://34.118.102.90:8443/api/v1/missings/'
url_search = 'https://34.118.102.90:8443/api/v1/coincidences/search/'
url_search_missing = 'https://34.118.102.90:8443/api/v1/missings?name=Микола&surname=Парасюк&father_name=Іванович&date_of_birth=2024-05-11'

response = requests.get(url_search, params={'missing_id': 6})
print(response.json())


data_json = {
  "source_url": "https://wanted.mvs.gov.ua/searchbezvesti/",
  "disappearance_date": "2024-05-11",
  "disappearance_place": "Донецька обл, Покровський район, с. Хапотронівка",
  "surname": "Парасюк",
  "name": "Микола",
  "father_name": "Іванович",
  "surname_rus": "Парасюк",
  "name_rus": "Николай",
  "father_name_rus": "Иванович",
  "date_of_birth": "2024-05-11",
  "gender": "male",
  "description": "Опис зовнішності",
  "special_data": "Особливі прикмети",
  "contact_data": "+380000000000"
}
response = requests.post(url_create_missing, data=json.dumps(data_json))
print(response.status_code)
print(response.json())
id = response.json()['missing_id']
file_data = open(f"./pictures/photo1.png", "rb").read()
response_post = requests.post(url_post, params={'missing_id': id, 'media_type': 'image/png'}, files={'file': file_data})
print(id)


for i in os.listdir(directory):
    with open(f"../Mix/pictures/{i}", "rb") as file:
        file_data = file.read()
    json_data = {
        "source_url": "https://youtube.com",
        "date_published": "2021-09-01"
    }
    response_create = requests.post(url_create, data=json.dumps(json_data))
    print(response_create.json())
    print(response_create.status_code)
    id = response_create.json()['coincidence_id']
    print(id)
    response_post = requests.post(url_post, params={"coincidence_id": id, "media_type": "image/jpg"}, files={"file": file_data})
    print(response_post.json())
    print(response_post.status_code)

response = requests.get('https://5284-31-144-168-144.ngrok-free.app/api/v1/missings/?name=%D0%9C%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0&surname=%D0%9F%D0%B0%D1%80%D0%B0%D1%81%D1%8E%D0%BA&father_name=%D0%86%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%D0%B8%D1%87&date_of_birth=2024-05-11')
print(response.json())