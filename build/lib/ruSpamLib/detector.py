import torch
import re
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name_default = 'NeuroSpaceX/ruSpam_V1mini'
model_name_average = 'NeuroSpaceX/ruSpam_V1average'
key = ""

default_model = AutoModelForSequenceClassification.from_pretrained(model_name_default, num_labels=1)
default_tokenizer = AutoTokenizer.from_pretrained(model_name_default)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
default_model.to(device)
default_model.eval()

def load_model_and_tokenizer(model_type='default'):
    if model_type == 'average':
        model_name = model_name_average
    else:
        model_name = model_name_default

    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=1)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model.to(device)
    model.eval()
    return model, tokenizer

def clean_text(text):
    text = re.sub(r'http\S+', '', text)  
    text = re.sub(r'[^А-Яа-я0-9 ]+', ' ', text)
    text = text.lower().strip()
    return text

def is_spam(message, key = "", model_type='default'):
    if model_type == "average":
        if key == "":
            print("Для использования данной модели передайте апи ключ. Купить тут: TG @NeuroSpaceX")
        else:
            import requests
            response = requests.get("https://ApiKeysServer-1.onrender.com/check_key", params={"api_key": key})

            if response.status_code == 200:
                model, tokenizer = load_model_and_tokenizer(model_type)
                message = clean_text(message)
                encoding = tokenizer(message, padding='max_length', truncation=True, max_length=128, return_tensors='pt')
                input_ids = encoding['input_ids'].to(device)
                attention_mask = encoding['attention_mask'].to(device)

                with torch.no_grad():
                    outputs = model(input_ids, attention_mask=attention_mask).logits
                    pred = torch.sigmoid(outputs).cpu().numpy()[0][0]
                return pred >= 0.5
            
            elif response.status_code == 403:
                print("Неверный API ключ.")
    elif model_type == "default":
        model, tokenizer = load_model_and_tokenizer(model_type)
        message = clean_text(message)
        encoding = tokenizer(message, padding='max_length', truncation=True, max_length=128, return_tensors='pt')
        input_ids = encoding['input_ids'].to(device)
        attention_mask = encoding['attention_mask'].to(device)

        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask).logits
            pred = torch.sigmoid(outputs).cpu().numpy()[0][0]
        return pred >= 0.5
    

    