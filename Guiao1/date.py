class Date:
    def __init__(self,day:int,month:int,year:int):
        try:
            if self.validDate(day,month,year):
                self.day = day
                self.month = month
                self.year = year
        except:
            print('Date does not exist!')
    def __str__(self):
        return ('(' if self.day> 9 else '(0' ) +f'{self.day}-'+ ('' if self.month> 9 else '0' )+f'{self.month}-{self.year})'
    def setDate(self,day,month,year):
       pass
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
        monthDayss = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        md = monthDayss[month-1]
        if Date.leapYear(year) and  month==2:
            md = 29
        return md
    @staticmethod
    def validDate(day,month,year):
        value = False
        if day>0 and day<=Date.monthDays(month,year):
            value = True
        return value
    def nextDay(self):
        if self.day+1<=self.monthDays(self.month,self.year):
            self.day+=1
        else:
            if self.month!=12:
                self.month+=1
                self.day=1
            else:
                self.month = 1
                self.year +=1
                self.day = 1

            #self.nextMonth()
            #self.nextYear()
    '''def nextMonth(self):
        if self.month!=12 and self.day==self.monthDays(self.month,self.year):
                self.month+=1
                self.day=1
        
    def nextYear(self):
        if self.month==12 and self.day == self.monthDays(self.month,self.year) :
            self.month = 1
            self.year +=1
            self.day = 1
    '''
    
    
    
def main():
    data1 = Date(28,2,2022)
    data2 = Date(31,12,2022)
    print(data1)
    print(data2,'\n\nnext day\n')
    data1.nextDay()
    data2.nextDay()
    print (data1)
    print(data2)
    for i in range(365): # verificar se funciona corretamente para um ano todo
        print(i)
        data1.nextDay()
        print(data1)
    print(data1.monthDays(12,2022))
    print(f"Month 2 of 2022 has {Date.monthDays(2, 2022)} days")

main()

