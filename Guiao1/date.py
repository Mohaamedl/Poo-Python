class Date:
    def __init__(self,day:int,month:int,year:int):
        try:
            if self.validDate(day,month,year):
                self.day = day
                self.month = month
                self.year = year
        except:
            print('Errrror')
    def __str__(self):
        return ('(' if self.day> 9 else '(0' ) +f'{self.day}-'+ ('' if self.month> 9 else '0' )+f'{self.month}-{self.year})'

    @staticmethod
    def validMonth(month):
        value = False
        if month>=1 and month<=12:
            value = True
        return value
        
    @staticmethod
    def leapYear(year):
        value = False
        if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 400 == 0 and year % 100 == 0):
            value = True
        return value
    @staticmethod
    def monthDays(month,year):
        monthDayss = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        md = monthDayss[month]
        if Date.leapYear(year) and  month==2:
            md = 29
        return md
    @staticmethod
    def validDate(day,month,year):
        value = False
        if day>0 and day<=Date.monthDays(month,year):
            value = True
        return value
    def increment(self,day,month,year):
        self.day+=day
        self.month += month
        self.year += year
    def decrement(self,day,month,year):
        self.day -=day
        self.month -=month
        self.year -= year
    def nextDay(self):
        self.increment(1,0,0)
    
    
    
def main():
    data1 = Date(28,2,2022)
    print(data1)
    data1.nextDay()
    print (data1)
    print(f"Month 2 of 2022 has {Date.monthDays(2, 2022)} days")

main()

