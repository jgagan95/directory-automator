import schedule, time, os, datetime, shutil

#based on the date, create a folder in a specific directory for each day in month
#obtain the date
full_date = datetime.date.today() #prints to year-month-day format
todays_date = f"{full_date}"[5:] #will give me just month-day format of date; is a string and not object anymore?
my_directory = 'C:\\Users\\Josh Agan\\Desktop\\Test'
todays_folder = f"{my_directory}\\{todays_date}" 
subtracted = datetime.timedelta(1)
new_day = full_date - subtracted
yesterdays_date = f'{new_day}'[5:]
yesterdays_folder = f"{my_directory}\\{yesterdays_date}"
pictures = ['2.jpg', '3.jpg']


#go into an already created folder and make a new directory based on the day
def create_folder():
  os.chdir(my_directory)
  os.mkdir(todays_date)

#transfer pictures from master directory into each folder created 
def transfer_pictures():
  if os.path.isdir(todays_folder):
    files = os.listdir(my_directory)
    for file in files:
      if file.endswith('.jpg'):
        shutil.copy(file, todays_folder)

#delete directories that are not used
def delete_directory():
  #if the folder created only has the two pictures transferred
  os.chdir(my_directory)
  if os.path.isdir(yesterdays_folder):
    files = os.listdir(yesterdays_folder)
    if files == pictures:
      shutil.rmtree(yesterdays_folder)
  #delete it

def job():
  delete_directory()
  create_folder()
  transfer_pictures()

schedule.every().day.at('15:56').do(job)

while True:
  schedule.run_pending()
  time.sleep(1)
