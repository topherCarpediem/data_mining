from threading import Timer
from datetime import datetime
from random import randrange
import send_email
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get('http://www.internetlivestats.com/')

class SetInterval:
    def __init__(self, func, sec):
        def wrapper():
            self.__init__(func, sec)
            func()
            self.t = Timer(sec, func)

        self.t = Timer(sec, wrapper)
        self.t.start()

    def stop(self):
        self.t.cancel()




def get_data():
    fb_user = ''
    google_user = ''
    twitter_user = ''

    source = BeautifulSoup(browser.page_source, 'lxml')

    rule = '%I:%M %p'
    formatted_time = datetime.now().time().strftime(rule)

    with open('facebook.txt', 'a') as result:
        for users in source.find_all("span", {"rel": "facebook_users"}):
            for digit in users.find_all("span", {"class":"rts-nr-int"}):
                fb_user = "{}{}".format(fb_user,digit.text)    
        result.write(formatted_time + ' ' + str(fb_user) + '\n')
    
    with open('google.txt', 'a') as result:
        for users in source.find_all("span", {"rel": "google_users"}):
            for digit in users.find_all("span", {"class":"rts-nr-int"}):
                google_user = "{}{}".format(google_user,digit.text)  
        result.write(formatted_time + ' ' + str(fb_user) + '\n')
    
    with open('google.txt', 'a') as result:
        for users in source.find_all("span", {"rel": "twitter_users"}):
            for digit in users.find_all("span", {"class":"rts-nr-int"}):
                twitter_user = "{}{}".format(twitter_user,digit.text)
        result.write(formatted_time + ' ' + str(fb_user) + '\n')

    print("Facebook active users {} {}".format(formatted_time,fb_user))
    print("Google active users {} {}".format(formatted_time,google_user))
    print("Twitter active users {} {}".format(formatted_time,twitter_user))
    print("================================================")
    

logger = SetInterval(get_data, 5.0)






# def get():
#     #   get the current time
#     rule = '%I:%M %p'
#     formatted_time = datetime.now().time().strftime(rule)
#
#     # source = open("source.txt", "r")
#     content = randrange(0, 3500)
#
#     with open('result.txt', 'a') as result:
#         print(formatted_time + ' ' + str(content))
#         result.write(formatted_time + ' ' + str(content) + '\n')
#
#         if 500 <= int(content) <= 1000:
#             print("Sending an email")
#             #send_email.send(content, "This number is fine")
#         elif 1000 <= int(content) <= 2000:
#             print("Sending an email")
#             #send_email.send(content, "Warning these number is close to the limit")
#         elif int(content) >= 3000:
#             print("Sending an email")
#             #send_email.send(content, "Oh! limit is reached")



#logger = SetInterval(get, 0.50)







