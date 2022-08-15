"""This module give us possibility to make calculations of
of cash remained and also calories remained """

import datetime as dt

today = dt.datetime.today().date()
day_week_ago = today - dt.timedelta(days=6)


class Records:
    """Class for saving the records"""
    
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment      
        if date == None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        

class Calculator():
    """Class with main logic of calculation"""
    
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.dayStats = []
        self.weekStats = []
        
    def add_record(self, record):
        """Function for addiing the records in list"""
        self.records.append(record)        
        return self.records

    def get_today_stats(self):
        """Function for getting the statistics for the whole that day"""
        for record in self.records:
            if record.date == today:
                self.dayStats.append(record.amount)
        return sum(self.dayStats)
                
    def get_week_stats(self):
        """Function for getting the statistics for previous week"""
        for record in self.records:
            if day_week_ago <= record.date < today:
                self.weekStats.append(record.amount)
        return sum(self.weekStats)
     
     
class CashCalculator(Calculator):
    """Class with functions for cash statistics"""

    usd_rate = 62.25
    euro_rate = 63.88
                
    def get_today_cash_remained(self, currency):
        """Function for calculation of your cash balance at this moment"""
        limit = self.limit
        dayStatsSum = self.get_today_stats()  
        difference = limit - dayStatsSum
       
        if currency == 'USD': #converting currency to 'RUB'
            N = difference * self.usd_rate
        elif currency == 'EURO':
            N = difference * self.euro_rate
        elif currency == 'RUB':
            N = difference
        
        if dayStatsSum < limit:
            return f'На сегодня осталось {N} рублей :)'
        elif dayStatsSum == limit:
            return 'Денег нет, но вы держитесь :/'
        else:
            return f'Денег нет, но вы держитесь. Долг {N} рублей'
        
class CaloriesCalculator(Calculator):
    """Class with functions for calories statistics"""

    def get_calories_remained(self):
        """Function for calculation your calories balance at this moment"""
        dayStats = self.get_today_stats()
        limit = self.limit
        N = limit - dayStats
        
        if dayStats < limit:
            return (f'Сегодня можно съесть еще что-нибудь,'
                   f'но с общей каллорийностью не более {N} кКал :)')
        else:
            return 'Хватит есть! :/'

if __name__ == '__main__':

    cash = CashCalculator(500)

    cash.add_record(Records(amount = 250,
                           comment = 'кафе',
                           date = '14.08.2022'))

    cash.add_record(Records(amount = 50,
                           comment = 'продукты',
                           date = '14.08.2022'))

    cash.add_record(Records(amount = 200,
                           comment = 'йога',
                           date = '14.08.2022'))

    print(cash.get_today_cash_remained('USD'))