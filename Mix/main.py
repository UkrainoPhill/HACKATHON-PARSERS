import os
import json
import base64


def main():
    directory = "D:/Workspace/ParseFaceBook/pictures"
    with open("missing_people.json", "r", encoding="utf-8") as json_file:
        missing_json = json.load(json_file)

    files = os.listdir(directory)
    for i, item in enumerate(missing_json):
        if i < len(files):
            with open(f"{directory}/{files[i]}", "rb") as file:
                file_data = file.read()
            # Convert the binary data to base64 before storing it in JSON
            item['image'] = base64.b64encode(file_data).decode('utf-8')
        else:
            break

    with open("updated_missing_people.json", "w", encoding="utf-8") as json_file:
        json.dump(missing_json, json_file, ensure_ascii=False, indent=4)

main()