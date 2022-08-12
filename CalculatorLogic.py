import datetime as dt

dt.datetime.today()

class Calculator:
    
    def __init__(self, limit):
       
        self.limit = limit
        self.records = []
        self.dayStats = 0
        self.weekStats = 0
        
    def add_record(self, records):
        
        self.records.append(records)        
        return records

    def get_today_stats(self):
        
        if self.date == dt.datetime.today():
            dayStats = dayStats + self.amount
        return dayStats
                
    def get_week_stats():
        pass
     
class Records(Calculator):

    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        self.date = date

        if date == None:
            self.date = dt.datetime.today()
        
        self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class CashCalculator(Calculator):
    
    def get_today_cash_remained(currency):
        
        N = limit - dayStats
        if dayStats < limit:
            return f'На сегодня осталось {N} {currency} :)'
        elif dayStats == limit:
            return 'Денег нет, держись :/'
        else:
            return f'Денег нет, держись. Твой долг {N} {currency}'


class CaloriesCalculator(Calculator):
    
    def get_calories_remained():
        N = limit - dayStats
        if dayStats < limit:
            return f'Сегодня можно съесть еще что-нибудь, но с общей каллорийностью не более {N} кКал :)'
        else:
            return 'Хватит есть! :/'
   
cash = CashCalculator(5000)

cash.add_record(Records(amount = 1500, comment = 'кафе', date = '08.03.22'))

cash.add_record(Records(amount = 500, comment = 'продукты', date = '08.03.22'))

cash.add_record(Records(amount = 2000, comment = 'йога', date = '08.03.22'))

print(cash.get_today_stats())