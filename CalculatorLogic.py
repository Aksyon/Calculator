```
"""This module give us possibility to make calculations of
of cash remained and also calories remained."""

import datetime as dt

DATE_FORMAT = '%d.%m.%Y'

class Records():
    """Class for saving the records."""

    def __init__(self, amount: float, comment: str, date: str = None) -> str:
        self.amount = amount
        self.comment = comment   
        if date is None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT).date()
        

class Calculator():
    """Class with main logic of calculation."""
    
    def __init__(self, limit: float) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, record: str):
        """Function for addiing the records in list."""
        self.records.append(record)        

    def get_today_stats(self) -> float:
        """Function for getting the statistics for the whole this day."""
        today = dt.datetime.today().date()
        return sum(record.amount for record in self.records if
            record.date == today
            )

    def get_week_stats(self) -> float:
        """Function for getting the statistics for previous week."""
        today = dt.datetime.today().date()
        day_week_ago = today - dt.timedelta(days=6)
        return sum(amount for amount in self.records if day_week_ago 
            <= amount.date < today
            )

    def get_difference(self) -> float:
        return self.limit - self.get_today_stats()
    

class CashCalculator(Calculator):
    """Class with functions for cash statistics."""
    CURRENCY = {'USD' : (62.25, 'в рублях'),
                'EURO' : (63.88, 'в рублях'),
                'CNY' : (8.67, 'в рублях'),
                'KZT' : (0.13, 'в рублях'), 
                'RUB' : (1, 'в рублях')
        }
    CASH_BALANCE_PLUS = 'На сегодня осталось {currency_name}: {balance} :)'
    CASH_BALANCE_MINUS = ('Денег нет, но вы держитесь. Долг {currency_name}: '
                         '{balance} :(')
    CASH_BALANCE_ZERO = 'Денег нет, но вы держитесь :/'

    def get_today_cash_remained(self, currency: str = 'RUB') -> str:
        """Function for calculation of your cash balance at this moment."""               
        try:
            currency_rate = self.CURRENCY[currency]
        except KeyError:
            raise KeyError(f'Вы ввели не поддерживаемую валюту: {currency}')

        cash_remained = self.get_difference() * currency_rate[0]
        
        if self.get_difference() == 0:
            return self.CASH_BALANCE_ZERO

        if self.get_difference() > 0:
            return self.CASH_BALANCE_PLUS.format(
                currency_name=currency_rate[1],
                balance=cash_remained
                )
        return self.CASH_BALANCE_MINUS.format(
            currency_name=currency_rate[1],
            balance=cash_remained
            )

        
class CaloriesCalculator(Calculator):
    """Class with functions for calories statistics."""
    CALORIES_BALANCE = ('Сегодня можно съесть еще что-нибудь, но с общей'
                       'каллорийностью не более {balance} кКал :)')
    STOP_EATING = 'Хватит есть! :/'

    def get_calories_remained(self) -> str:
        """Function for calculation your calories balance at this moment."""
        if self.get_difference() > 0:
            return self.CALORIES_BALANCE.format(balance=self.get_difference())
        return self.STOP_EATING

if __name__ == '__main__':

    cash = CashCalculator(500)

    cash.add_record(Records(amount = 600,
                           comment = 'кафе',
                           date = '26.08.2022'))

    cash.add_record(Records(amount = 50,
                           comment = 'продукты',
                           date = '20.08.2022'))

    cash.add_record(Records(amount = 250,
                           comment = 'йога',
                           date = '20.08.2022'))
       
    print(cash.get_today_cash_remained('USD'))
```