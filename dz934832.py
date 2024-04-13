class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_usd(self, amount_in_uah):
        return amount_in_uah / self.exchange_rate


if __name__ == "__main__":
    exchange_rate = 39.52
    converter = CurrencyConverter(exchange_rate)

    amount_in_uah = float(input("Введите количество гривен: "))
    amount_in_usd = converter.convert_to_usd(amount_in_uah)

    print(f"{amount_in_uah} гривен равно {amount_in_usd} долларам")