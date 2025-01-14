import yagmail , pandas
from news import NewsFeed
import datetime
import time 

while True :

    if datetime.datetime.now().hour == 11 and datetime.datetime.now().minute == 24 :
        df = pandas.read_excel('people.xlsx')

        for index,rows in df.iterrows():
            news_feed = NewsFeed(intrest=rows['interest'],
                                from_date=datetime.datetime.now() - datetime.timedelta(days=1),
                                to_date=datetime.datetime.now().strftime("%Y-%m-%d") )

            email = yagmail.SMTP(user = "pythonpractice529@gmail.com",password = 'xpwm cevy bpiu egsw')

            email.send(to=rows['email'], 
                        subject = f"Hi {rows['name']}!!",
                        contents = f"Your Intrest:{rows['interest']} of the day !!\n See what's on about {rows['interest']} \n\n {news_feed.get()}",
                        attachments = 'design.txt'
                    )

    time.sleep(60)
