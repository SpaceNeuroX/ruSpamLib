import requests

class SpamChecker:
    def __init__(self, user_token, model_name='ruSpam-turbo-test'):
        """
        Инициализация объекта SpamChecker.

        :param user_token: API токен для аутентификации.
        :param model_name: Имя модели для анализа (по умолчанию: 'spamNS_v6').
        """
        self.user_token = user_token
        self.model_name = model_name
        self.api_urls = [
            "https://neurospacex-ruspamtwo.hf.space/api/check_spam",
            "https://neurospacex-ruspam.hf.space/api/check_spam"
        ]
        self.selected_server = self._initialize_server()

    @staticmethod
    def _calculate_overall_load(data):
        """
        Рассчитывает общую нагрузку сервера.

        :param data: Словарь с данными о нагрузке (CPU, память, диск).
        :return: Средняя нагрузка в процентах.
        """
        try:
            cpu = data.get("cpu_usage_percent", 0)
            memory = data.get("memory_usage_percent", 0)
            disk = data.get("disk_usage_percent", 0)
            return round((cpu + memory + disk) / 3, 2)
        except Exception:
            return None

    @staticmethod
    def _get_server_load(status_url):
        """
        Получает текущую нагрузку сервера.

        :param status_url: URL для получения статуса сервера.
        :return: Процент загрузки сервера или None, если сервер недоступен.
        """
        try:
            response = requests.get(status_url)
            if response.status_code == 200:
                data = response.json()
                return SpamChecker._calculate_overall_load(data)
            else:
                print(f"Failed to get load from {status_url}, status code: {response.status_code}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error getting server load from {status_url}: {e}")
            return None

    def _initialize_server(self):
        """
        Выбирает сервер с наименьшей нагрузкой из списка доступных.

        :return: URL выбранного сервера или None, если все сервера недоступны.
        """
        server_loads = {
            url: self._get_server_load(url.replace("/api/check_spam", "/api/status")) 
            for url in self.api_urls
        }
        available_servers = {url: load for url, load in server_loads.items() if load is not None}
        selected = min(available_servers, key=available_servers.get, default=None)
        if selected:
            print(f"Selected server: {selected} with load {available_servers[selected]}%")
        else:
            print("No available servers found.")
        return selected

    def check_spam(self, message):
        """
        Проверяет, является ли сообщение спамом.

        :param message: Строка сообщения для анализа.
        :return: Словарь с результатами анализа.
        """
        if not self.user_token:
            print("API token is required for authentication.")
            return {
                "is_spam": False,
                "confidence": 0.0,
                "model_used": self.model_name,
                "tokens_used": 0,
                "cost": 0.0,
                "api_key": None,
            }

        if not self.selected_server:
            print("No server initialized.")
            return {
                "is_spam": False,
                "confidence": 0.0,
                "model_used": self.model_name,
                "tokens_used": 0,
                "cost": 0.0,
                "api_key": self.user_token,
            }

        headers = {
            "api-key": self.user_token
        }
        data = {
            "message": message,
            "model_name": self.model_name
        }

        try:
            response = requests.post(self.selected_server, json=data, headers=headers)
            if response.status_code == 200:
                result = response.json()
                print(f"Response received from server: {self.selected_server}")
                return {
                    "is_spam": result.get('is_spam', 0) == 1,
                    "confidence": result.get('confidence', 0.0),
                    "model_used": result.get('model_used', self.model_name),
                    "tokens_used": result.get('tokens_used', 0),
                    "cost": result.get('cost', 0.0),
                    "api_key": result.get('api_key', self.user_token),
                }
            else:
                print(f"Server at {self.selected_server} failed with status code {response.status_code}.")
                if response.status_code == 400:
                    result = response.json()
                    if 'error' in result:
                        print(f"Error: {result['error']}")
        except requests.exceptions.RequestException as e:
            print(f"Network error while connecting to {self.selected_server}: {e}")

        print("Failed to process the request.")
        return {
            "is_spam": False,
            "confidence": 0.0,
            "model_used": self.model_name,
            "tokens_used": 0,
            "cost": 0.0,
            "api_key": self.user_token,
        }
