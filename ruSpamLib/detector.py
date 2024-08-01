import requests

def is_spam(message, model_name='spamNS_v1'):
    api_url = "https://neurospacex-ruspamlib-server.hf.space/check_spam"
    
    payload = {
        "message": message,
        "model_name": model_name
    }
    
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result['is_spam'] == 1
    else:
        print("Ошибка при запросе к API:", response.status_code)
        if response.status_code == 400:
            result = response.json()
            if 'error' in result:
                print("Ошибка:", result['error'])
        return False
