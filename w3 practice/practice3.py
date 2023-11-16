import platform
import datetime

x = platform.system()
print(x)

x = datetime.datetime.now()
print(x)

print(x.strftime("%b"))
#print(x.day)
print(x.date)
