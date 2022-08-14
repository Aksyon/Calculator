import datetime as dt

today = dt.datetime.today().date()
day_week_ago = today - dt.timedelta(days = 6)

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
    
    def __init__(self, limit):
        
        Calculator.__init__(self, limit)
        self.usd_rate = 62.25
        self.euro_rate = 63.88
                
    def get_today_cash_remained(self, currency):
        limit = self.limit
        dayStatsSum = Calculator.get_today_stats(self)     # WTF? become 2 times more
        print(dayStatsSum)
        dif = limit - dayStatsSum
        
        if currency == 'USD':              #converting currency to 'RUB'
            N = dif * self.usd_rate
        elif currency == 'EURO':
            N = dif * self.euro_rate
        elif currency == 'RUB':
            N = dif
        
        if dayStatsSum < limit:
            return f'На сегодня осталось {N} рублей :)'
        elif dayStatsSum == limit:
            return 'Денег нет, но вы держитесь :/'
        else:
            return f'Денег нет, но вы держитесь. Долг {N} рублей'
        
class CaloriesCalculator(Calculator):
        
    def get_calories_remained():
        
        dayStats = Calculator.get_today_stats()
        limit = Calculator.limit
        N = limit - dayStats
        if dayStats < limit:
            return f'Сегодня можно съесть еще что-нибудь, но с общей каллорийностью не более {N} кКал :)'
        else:
            return 'Хватит есть! :/'
   
cash = CashCalculator(1000)

cash.add_record(Records(amount = 250, comment = 'кафе', date = '14.08.2022'))

#cash.add_record(Records(amount = 50, comment = 'продукты', date = '14.08.2022'))

#cash.add_record(Records(amount = 50, comment = 'йога', date = '14.08.2022'))

print(Calculator.get_today_stats(cash))
print(cash.get_today_cash_remained('RUB'))