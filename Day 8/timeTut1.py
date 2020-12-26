import time

# timeSecond = time.time()
# print("Epoch time is:",timeSecond)
#
# local_time = time.ctime(timeSecond)
# print(local_time)

local_time = time.localtime(time.time())
print(local_time)
print("Year -",local_time.tm_year)
print("Hour -",local_time.tm_hour)