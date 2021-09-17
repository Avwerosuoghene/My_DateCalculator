from datetime import datetime,date,time,timedelta
import sys
import math




def Days_Calculate():
    Year = int(input("Type the start year... "))
    Month = int(input("Type the start Month... "))
    Day = int(input("Type the start Day... "))
    
    Year2 = int(input("Type the end year... "))
    Month2 = int(input("Type the end Month... "))
    Day2 = int(input("Type the end Day... "))
    
    #Used try and except to catch exception errors
    try:
        Past_Period = date(Year, Month,Day)

        Present_Period = date(Year2, Month2, Day2)
    except:
        print("invalid time inputted")
        print ("Press 1 to quit or 2 to retry")
        step = input("Type here.. ")
        if "1" in step:
            return quit("See you next time")
        elif "2" in step:
            return Days_Calculate()
        else:
            pass


    Days_Past = Present_Period - Past_Period
    
    if Days_Past.days < 0:
        print ("I do not calculate future duration")
        print ("Press 1 to quit or 2 to retry")
        retry_days_calc = input("Type here.. ")
        if "1" in retry_days_calc:
            return quit("See you next time")
        elif "2" in retry_days_calc:
            return Days_Calculate()
    else:
        pass
    
    
    
    return print("The amount of days elapsed is {}".format(Days_Past.days))
    
    
#Calculates the duration/timespan in hours and minutes format
def Hours_Minute_Timing():
    #This line lets you input your value for day, hour and minute of the month
    
    day = int(input("start day.."))
    hour = int(input("start hour.."))
    minute = int(input("start minute.."))
    
    day2 = int(input("end day.."))
    hour2 = int(input("end hour.."))
    minute2 = int(input("end minute.."))
    Today = datetime.now()
    
    
    
    #Using try catches any exceptions/errors in the code
    #try:
        #The current date is assigned to the variable today, and the starting date is attached to the variable previous day
        
    #Using try catches any exceptions/errors in the code  
    try:
    
        End_day = datetime(Today.year, Today.month,day2,hour2,minute2)
        Start_day = datetime(Today.year,Today.month,day,hour,minute)
        
    except:
        print("Invalid entry"  )
        return run_time()
    
    Hours = 0
    Minutes = 0
    
    #Checks if the date being calculated is not today
    if End_day.day >= day:
        Hours = (End_day.day - day)*24 + int(End_day.hour)
        Real_Hours = Hours - hour
       
    else:
        print("I do not calculate future dates")
        return run_time()
        
    #if the day is today, subtract 24hours from the hours obtained from the datetime class 
    #Real_Hours =int(Today.hour) - hour
    
    #this calculates the minutes
    if End_day.minute < minute:
        x = minute - End_day.minute
        y = Real_Hours *60 -x
        
        
        #This assignes the decimal from the devision and the whole number to val1 and val2
        val1,val2 = math.modf(y/60)
        
        
        Real_Hours = int(val2)
        Minutes = val1 *60
        #rounding up the value from the decimal obtained using the round function
        Minutes = round(Minutes)
        
    else:  
        Minutes = int(End_day.minute) - minute
    
    return print ("The event took {} hours and {} minutes to resolve .".format(Real_Hours, Minutes))
    #except:
        #print("Invalid entry")
        
        
def quit(prompt):
    print(prompt)
    sys.exit()

def run_time():
    insert_your_options = input("What do you want to do? \n 1. Calculate Time Span in days \n 2. Calculate Time Duration in Minutes \n 3. To quit \n .... ")
    if "1" in insert_your_options:
        Days_Calculate()
    elif "2" in insert_your_options:
        Hours_Minute_Timing()
        
    elif "3" in insert_your_options:
        quit("See you next time")

    else:
        print("wrong option, please retry")
        run_time()
        
run_time()
    
