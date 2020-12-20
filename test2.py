import schedule, time, os, datetime

#based on the date, create a folder in a specific directory for each day in month
def job():
  #obtain the date
  full_date = datetime.date.today() #prints to year-month-day format
  todays_date = f"{full_date}"[5:] #will give me just month-day format of date; is a string and not object anymore?
  #go into an already created folder and make a new directory based on the day
  os.chdir('C:\\Users\\Josh Agan\\Desktop\\Test')
  os.mkdir(todays_date)

#creates the folder in 'Test' every day at 12:02 AM
schedule.every().day.at('00:02').do(job)

while True:
  schedule.run_pending()
  time.sleep(1)
