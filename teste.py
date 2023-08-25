from datetime import datetime

now = datetime.now().month
print(now)
print(datetime.strftime(now, '%m'))
