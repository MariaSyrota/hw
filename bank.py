import requests


class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                for currency in data:
                    if currency["cc"] == "USD":
                        return currency["rate"]
                raise ValueError("Курс не найден.")
            else:
                raise ConnectionError(f"Ошибка при запросе данных: {response.status_code}")
        except requests.exceptions.RequestException as ex:
            raise ConnectionError(f"Ошибка подключения: {ex}")

    def convert_to_usd(self, amount):
        if self.usd_rate is None:
            raise ValueError("Ошибка:")
        return amount / self.usd_rate


if __name__ == "__main__":
    try:
        converter = CurrencyConverter()
        print(f"Курс доллара: 1 USD = {converter.usd_rate:.2f} UAH")

        amount_uah = float(input("Введите количество гривен: "))
        amount_usd = converter.convert_to_usd(amount_uah)

        print(f"{amount_uah:.2f} UAH = {amount_usd:.2f} USD.")
    except Exception as e:
        print(f"Ошибка подключения:{e}")