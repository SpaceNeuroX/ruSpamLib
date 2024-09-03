
# Spam Detection Library

Это официальная библиотека для обнаружения спама от организации https://huggingface.co/NeuroSpaceX. Она предоставляет удобные средства для проверки сообщений на спам с использованием моделей, доступных на платформе Hugging Face.

## Установка

Для установки библиотеки используйте pip:

```bash
pip install ruSpam
```

## Пример использования

```python
from ruSpamLib import is_spam

message = input("Введите сообщение: ")

pred_average = is_spam(message, model_name="spamNS-mini-turbo_v2")

print(f"Prediction: {'Spam' if pred_average else 'Not Spam'}")
```

## Модели 

1. spamNS_v1
2. spamNS_large_v3
3. spamNS-mini-turbo_v1
4. spamNS-mini-turbo_v2

Вы можете передать параметр multi_model=True в функцию is_spam, чтобы использовать все доступные модели одновременно. Это может повысить точность детекции спама, однако не обязательно указывать конкретную модель. Пример использования:

```python
from ruSpamLib import is_spam

message = input("Введите сообщение: ")

pred_average = is_spam(message, multi_model=True)

print(f"Prediction: {'Spam' if pred_average else 'Not Spam'}")
```
