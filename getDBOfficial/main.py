import json

from pyrogram import Client
def main():
    app = Client(
        "my_account",
        api_id=22007863,
        api_hash="6d3380f87b200037f7a4d1d8e7667518"
    )
    channel_id = -1001582277245
    id = {}
    with open("id.json", "w") as f:
        f.write("[")
    with app:
        for message in app.get_chat_history(channel_id):
            if message.photo:
                id["id"] = message.id
                id['date'] = str(message.date)
                json.dump(id, open("id.json", "a"))
                with open("id.json", "a") as f:
                    f.write(",")
                app.download_media(message.photo, file_name=f"{message.id}.png")

main()