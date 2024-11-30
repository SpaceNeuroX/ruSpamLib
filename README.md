
# Spam Detection Library

Это официальная библиотека для обнаружения спама от организации https://huggingface.co/NeuroSpaceX. Она предоставляет удобные средства для проверки сообщений на спам с использованием моделей машиного обучения.

## Установка

Для установки библиотеки используйте pip:

```bash
pip install ruSpam
```

## Пример использования

```python
from ruSpamLib import is_spam

message = input("Введите сообщение: ")

pred_average, confidence = is_spam(message, model_name="spamNS_v6")

print(f"Prediction: {'Spam' if pred_average else 'Not Spam'}")
```

## Модели 

1. spamNS_v1
2. spamNS_v6

Лицензия и использование
При использовании библиотеки в некоммерческих проектах необходимо указывать автора библиотеки — NeuroSpaceX.
