#finding weekday for a valid date
import calendar
def check_leap(y):
    if y%100==0:
        if y %400==0:
            return True
        else:
            return False
    else:
        if y% 4==0:
            return True 
        else:
            return False

def check_valid_date(dt,m,y,l):
    if l:
        if m==2:
            if dt<30:
                return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if dt<32:
                       return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if m%2==0:
                    if dt<32:
                       return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
    else:
        if m==2:
            if dt<29:
                if dt<30:
                    return True
            else:
                return False
        else:
            if m<8:
                if m%2==1:
                    if dt<32:
                       return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False
            else:
                if m%2==0:
                    if dt<32:
                       return True
                    else:
                        return False
                else:
                    if dt<31:
                        return True
                    else:
                        return False

def get_day(day_index):
    list_of_days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    return list_of_days[day_index]

while(1):
    
    year=int(input(" Enter a year from 1970 "))
    if year<1970:
        print("enter a valid year")
    else:
        break

while(1):
    
    month=int(input(" Enter a month(1-12) "))
    if month<=12 and month>0:
        break
    else:
        print("enter a valid month")
        
leap=check_leap(year)
while(1):
    
    date=int(input(" Enter a date "))
    if date>0 and check_valid_date(date,month,year,leap):
        break
    else:
        print("enter a valid date")
    
day_index=calendar.weekday(year,month,date)
day=get_day(day_index)
print(date,"/",month,"/",year,"falls on",day)               
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            