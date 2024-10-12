import requests

def is_spam(message, model_name='spamNS_v6', multi_model=False):
    if multi_model:
        api_url = "https://neurospacex-ruspamlib-serverandsite.hf.space/api/check_spam_all"
        payload = {
            "message": message
        }
    else:
        api_url = "https://neurospacex-ruspamlib-serverandsite.hf.space/api/check_spam"
        payload = {
            "message": message,
            "model_name": model_name
        }
    
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        result = response.json()
        if multi_model:
            is_spam_result = result.get('classification', '') == 'spam'
            confidence = result.get('confidence', 0)
        else:
            is_spam_result = result.get('is_spam', 0) == 1
            confidence = result.get('confidence', 0)
        
        return is_spam_result, confidence
    else:
        print("Ошибка при запросе к API:", response.status_code)
        if response.status_code == 400:
            result = response.json()
            if 'error' in result:
                print("Ошибка:", result['error'])
        return False, 0 
