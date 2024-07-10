class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount
        print(f"Теперь ваш баланс составляет: {self._balance}")

    def _kill(self):
        self._balance = 0
        print("Все деньги были обнулены.")

    def __jackpot(self):
        self._balance *= 10
        print(f"Вы выиграли джекпот! Новый баланс: {self._balance}")

    def _merge_balance(self, other):
        self._balance += other._balance
        other._balance = self._balance

# Тестирование функциональности класса Bank
if __name__ == "__main__":
    client1 = Bank("Alice", 100)
    client2 = Bank("Bob", 200)

    print(f"Баланс клиента {client1._name}: {client1._balance}")
    print(f"Баланс клиента {client2._name}: {client2._balance}")

    client1.moneyX()
    client2._kill()
    client1._merge_balance(client2)

    print(f"Новый баланс клиента {client1._name}: {client1._balance}")
    print(f"Новый баланс клиента {client2._name}: {client2._balance}")

    # client1.__jackpot() # Не доступен извне класса Bank
