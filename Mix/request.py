import json
import requests

# Load the JSON data
with open("missing_people.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

url_create_missing = 'https://34.118.102.90:8443/api/v1/missings/'

for i, item in enumerate(json_data):
    data = {
        "source_url": "https://wanted.mvs.gov.ua/searchbezvesti/",
        "disappearance_date": item['disappearance_date'],
        "disappearance_place": item['disappearance_place'],
        "surname": item['surname'],
        "name": item['name'],
        "father_name": item['father_name'],
        "surname_rus": item['surname_rus'],
        "name_rus": item['name_rus'],
        "father_name_rus": item['father_name_rus'],
        "date_of_birth": item['date_of_birth'],
        "gender": item['gender'],
        "description": item['description'],
        "special_data": item['special_data'],
        "contact_data": item['contact_data']
    }
    response_user = requests.post(url_create_missing, data=json.dumps(data))
    user_id = int(response_user.json()['missing_id'])
    url_upload_photo = f'https://34.118.102.90:8443/api/v1/uploads'
    files = {'file': open(f'D:/Workspace/ParseFaceBook/pictures/photo{i+1}.png', 'rb')}
    response_photo = requests.post(url_upload_photo, files=files, params={'missing_id': user_id, 'media_type': 'image/png'})

