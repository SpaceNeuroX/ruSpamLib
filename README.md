
# Spam Detection Library

Это официальная библиотека для обнаружения спама от организации [NeuroSpaceX](https://huggingface.co/NeuroSpaceX). Она предоставляет удобные средства для проверки сообщений на спам с использованием моделей машинного обучения.

## Установка

Для установки библиотеки используйте pip:

```bash
pip install ruSpam
```

## Пример использования

```python
from ruSpamLib import SpamChecker

user_token = "ВАШ_ТОКЕН"

checker = SpamChecker(user_token=user_token, model_name='ruSpam-turbo-test')

message = "Это пример сообщения для анализа."

result = checker.check_spam(message)

print(result)
```

## Модели 

1. spamNS_v1
2. spamNS_v6
3. spamNS_v7
4. spamNS_v7_tiny
5. spamNS_v8_beta
6. ruSpam-turbo-test

## Лицензия и использование

При использовании библиотеки в некоммерческих проектах необходимо указывать автора библиотеки — NeuroSpaceX.

Наша последняя модель, `ruSpam-turbo-test`, обучена на более чем 2,5 миллионах сообщений и значительно превосходит предыдущие версии.

Чтобы купить токен, напишите боту @ruSpamNS_bot в Telegram команду `/buy_token <сумма>`, оплатите по предоставленной ссылке, а затем нажмите кнопку "Проверить платеж". После успешной оплаты бот выдаст вам API-ключ.

Чтобы посмотреть оставшийся баланс API-ключа, введите команду `/token_balance`.

Стоимость проверки составляет 0,04 рубля за каждые 128 токенов текста.

Вопросы или ошибки? Пишите @NeuroSpaceX.

Официальный бот для удаления рекламы и спама в группах: @ruSpamNS_bot

## Установка библиотеки

Для установки используйте:

```bash
pip install ruSpam
```

## Ссылка на код библиотеки

[GitHub: ruSpam](https://github.com/NeuroSpaceX/ruSpam)
