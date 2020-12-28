from plyer import notification
import time

def alwaysNotifyMe():
    notification.notify(
        title= "Its time for Handwash",
        message ='As per WHO guidelines, every 2 hours you should do handwash using soap',
        app_icon="C:/Users/Admin/Desktop/handwash.ico",
        timeout = 5
    )


while True:
    alwaysNotifyMe()
    time.sleep(20)


