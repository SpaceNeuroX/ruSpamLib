
# Spam Detection Library

Это официальная библиотека для обнаружения спама от организации [RUSpam](https://huggingface.co/RUSpam). Она предоставляет удобные средства для проверки сообщений на спам с использованием моделей, доступных на платформе Hugging Face.

## Установка

Для установки библиотеки используйте pip:

```bash
pip install ruSpam
```

## Доступные модели

В библиотеке доступны следующие модели:

1. spamNS_v1
2. spam_deberta_v4

## Пример использования

```python
from ruSpamLib import is_spam

message = input("Введите сообщение: ")

pred_average = is_spam(message, model_name="spam_deberta_v4")

print(f"Prediction: {'Spam' if pred_average else 'Not Spam'}")
```

## Разработчики

1. spamNS_v1 - разработчик [NeuroSpaceX](https://t.me/NeuroSpaceX)
2. spam_deberta_v4 - разработчик [bceloss](https://t.me/bceloss)
