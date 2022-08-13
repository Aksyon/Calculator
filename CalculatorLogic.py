import datetime as dt

today = dt.datetime.today().date()
day_week_ago = today - dt.timedelta(days = 6)

class Records:

    def __init__(self, amount, comment, date):
        
        self.amount = amount
        self.comment = comment
                
        if date == None:
            date = dt.datetime.today()
        else:
            date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.date = date
        
class Calculator():
    
    def __init__(self, limit):
       
        self.limit = limit
        self.records = []
        self.dayStats = 0
        self.weekStats = 0
        
    def add_record(self, records):
        
       self.records.append(records)        
       return records

    def get_today_stats():
        
        date = Records.date
       
        if date == dt.datetime.today():
            dayStats = dayStats + amount
            return dayStats
                
    def get_week_stats():
       
        if day_week_ago < day < today:
            weekStats = weekStats + amount
            return weekStats 
     
class CashCalculator(Calculator):
    
    def __init__(self, limit, usd_rate = 62.25, euro_rate = 63.88):
        
        Calculator.__init__(self, limit)
        self.usd_rate = usd_rate
        self.euro_rate = euro_rate
        
    def get_today_cash_remained(currency):
        
        N = limit - dayStats

        if currency == 'USD':
            N = N * usd_rate
        elif currency == 'EURO':
            N = N * euro_rate

        if dayStats < limit:
            return f'На сегодня осталось {N} рублей :)'
        elif dayStats == limit:
            return 'Денег нет, держись :/'
        else:
            return f'Денег нет, держись. Твой долг {N} рублей'

class CaloriesCalculator(Calculator):
        
    def get_calories_remained():
        
        dayStats = Calculator.get_today_stats
        limit = Calculator.limit
        N = limit - dayStats
        if dayStats < limit:
            return f'Сегодня можно съесть еще что-нибудь, но с общей каллорийностью не более {N} кКал :)'
        else:
            return 'Хватит есть! :/'
   
cash = CashCalculator(5000)

cash.add_record(Records(amount = 1500, comment = 'кафе', date = '08.03.2022'))

cash.add_record(Records(amount = 500, comment = 'продукты', date = '08.03.2022'))

cash.add_record(Records(amount = 2000, comment = 'йога', date = '08.03.2022'))

print(Calculator.get_today_stats())