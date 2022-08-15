import datetime as dt

today = dt.datetime.today().date()
day_week_ago = today - dt.timedelta(days=6)

class Records:
    
    
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment      
        if date == None:
            self.date = dt.datetime.today().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        
        
class Calculator():
    
    
    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.dayStats = []
        self.weekStats = []
        
    def add_record(self, record):
       self.records.append(record)        
       return self.records

    def get_today_stats(self):
        for record in self.records:
            if record.date == today:
                self.dayStats.append(record.amount)
        return sum(self.dayStats)
                
    def get_week_stats(self):
        for record in self.records:
            if day_week_ago <= record.date < today:
                self.weekStats.append(record.amount)
        return sum(self.weekStats)
     
class CashCalculator(Calculator):
    

    usd_rate = 62.25
    euro_rate = 63.88
                
    def get_today_cash_remained(self, currency):
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


    def get_calories_remained(self):
        
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