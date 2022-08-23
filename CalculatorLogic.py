"""This module give us possibility to make calculations of
of cash remained and also calories remained """

import datetime as dt
FORMAT = '%d.%m.%Y'


class Records():
    """Class for saving the records"""
    
    def __init__(self, amount, comment, date):
        self.amount = float(amount)
        self.comment = str(comment)     
        if date is None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, FORMAT).date()
        

class Calculator():
    """Class with main logic of calculation"""
    
    def __init__(self, limit):
        self.limit = int(limit)
        self.records = []
        self.dayStats = []
        self.ad = 0

    def add_record(self, record):
        """Function for addiing the records in list"""
        self.records.append(record)        
        return self.records

    def get_today_stats(self):
        """Function for getting the statistics for the whole this day"""
        composeDayStats = [amount for amount in self.records if amount.date ==
                          dt.datetime.today().date()]
        return sum(composeDayStats)

    def get_week_stats(self):
        """Function for getting the statistics for previous week"""
        today = dt.datetime.today().date()
        day_week_ago = today - dt.timedelta(days=6)
        composeWeekStats = [amount for amount in self.records if day_week_ago 
                           <= amount.date < today]
        return sum(composeWeekStats)

    def getDifference(self):
        getDaySum = self.get_today_stats()
        isDifference = self.limit - getDaySum
        return isDifference
    

class CashCalculator(Calculator):
    """Class with functions for cash statistics"""
    CURRENCY = {'USD_RUB' : [62.25, 'в рублях'],
                'EURO_RUB' : [63.88, 'в рублях'],
                'USD_EURO' : [1, 'в евро'],
                'EURO_USD' : [1, 'в долларах'],
                'RUB' : [1, 'в рублях']
    }
    CASH_BALANCE_PLUS = 'На сегодня осталось {currency_name}: {balance}'
    CASH_BALANCE_MINUS = ('Денег нет, но вы держитесь. Долг {currency_name}: '
                         '{balance}')
    CASH_BALANCE_ZERO = 'Денег нет, но вы держитесь :/'
    
    def get_today_cash_remained(self, currency):
        """Function for calculation of your cash balance at this moment"""
        isDifference = self.getDifference()
        getRate = self.CURRENCY[currency]
        getCashRemained = isDifference * getRate[0]
      
        if getCashRemained != 0:
            if getCashRemained > 0:
                return self.CASH_BALANCE_PLUS.format(
                    currency_name = getRate[1], balance=getCashRemained)
            return self.CASH_BALANCE_MINUS.format(
                currency_name = getRate[1], balance=getCashRemained)
        if getCashRemained == 0:
            return self.CASH_BALANCE_ZERO

        
class CaloriesCalculator(Calculator):
    """Class with functions for calories statistics"""
    CALORIES_BALANCE = ('Сегодня можно съесть еще что-нибудь, но с общей'
                       'каллорийностью не более {balance} кКал :)')
    STOP_EATING = 'Хватит есть! :/'

    def get_calories_remained(self):
        """Function for calculation your calories balance at this moment"""
        isDifference = self.getDifference()        
        if isDifference > 0:
            return self.CALORIES_BALANCE.format(balance=isDifference)
        return self.STOP_EATING

if __name__ == '__main__':

    cash = CashCalculator(500)

    cash.add_record(Records(amount = 500,
                           comment = 'кафе',
                           date = '22.08.2022'))

    cash.add_record(Records(amount = 50,
                           comment = 'продукты',
                           date = '20.08.2022'))

    cash.add_record(Records(amount = 250,
                           comment = 'йога',
                           date = '20.08.2022'))
       
    print(cash.get_today_cash_remained('USD_EURO'))