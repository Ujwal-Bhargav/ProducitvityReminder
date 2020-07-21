from crontab import CronTab
cron = CronTab(user='ujwaltadur')
job = cron.new(command='python3 Documents/Learning/Python/Alert.py')
job.minute.every(5)
cron.write()
print(job.enable())