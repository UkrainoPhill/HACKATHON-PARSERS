import json
import requests

url_create = 'https://34.118.102.90:8443/api/v1/coincidences/'
url_upload = 'https://34.118.102.90:8443/api/v1/uploads/'

with open('../ParseTG/id.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

for item in json_data:
    data = {
        'source_url': "https://t.me/bazaFIO/" + f"{item['id']}",
        'date_published': item['date']
    }
    response = requests.get(url_create, data=json.dumps(data))
    upload_ids = response.json()['upload_ids']
    for i in enumerate(json_data['id']):
        files = {'file': open(f'../ParseTG/photos/{i}', 'rb')}
        response = requests.post(url_upload, files=files, params={'coincidence_id': response.json()['coincidence_id'], 'media_type': 'image/png'})
        print(response.json())
