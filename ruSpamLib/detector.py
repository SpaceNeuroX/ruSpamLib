import requests

def is_spam(message, key="", model_type='default'):
    api_url = "https://neurospacex-keysapiserv.hf.space/check_spam"
    
    payload = {
        "message": message,
        "api_key": key,
        "model_type": model_type
    }
    
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result['is_spam'] == 1
    elif response.status_code == 403:
        result = response.json()
        if 'detail' in result and result['detail'] == 'Invalid API key':
            print("Неверный API ключ.")
        else:
            print("Ошибка при запросе к API:", result.get('detail', 'Неизвестная ошибка'))
    else:
        print("Ошибка при запросе к API:", response.status_code)
    
    return False
    

    