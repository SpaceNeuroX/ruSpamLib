import requests
import json

api_url = "https://neurospacex-keysapiserv.hf.space/check_spam"
api_key = "6319e4ed05caddc6ee144bb5вf6e2f924ced1765473e837dc0d0b46e7c1e72071" 
message = """🎁НОВИЧКАМ ВЕЗЕТ🎁
Как всем известно, когда появляется новый казик, он выдает лучше чем те, что уже есть на рынке.
Это делается для того, чтобы привлечь новых людей!
Вот и я решил проверить эту теорию на новом казике PUNCH.  (https://bit.ly/46rZi5o)👊
Результат удивил, с первого же депозита получился неплохой занос, смотри в видео выше! ⬆️
Проверь сам пока не поздно! Я бы поторопился 😄"""
model_type = "average"

payload = {
    "message": message,
    "api_key": api_key,
    "model_type": model_type
}

response = requests.post(api_url, json=payload)

print(response.json())
