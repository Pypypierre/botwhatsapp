import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import threading
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\pjduh\\AppData\\Local\\Google\\Chrome\\User Data\\")
options.add_argument("profile-directory=Default")
options.headless = False
driver = webdriver.Chrome(executable_path=r'\Users\pjduh\PycharmProjects\webscraping\chromedriver.exe', options=options)

def init():
    driver.get("https://web.whatsapp.com/")
    driver.implicitly_wait(20)
    driver.find_element_by_xpath("//*[contains(text(), 'Testbot')]").click()
    driver.implicitly_wait(10)
    d = "{}".format(datetime.datetime.now())
    date = datetime.datetime.now()
    mm = date.minute
    hh = date.hour
    tim = "[{}:{}, {}/{}/{}]".format(hh, mm, d[8:10], d[5:7], d[0:4])
    print(tim," Software of Pierre-Jean:")
    loop()

def searching():
    x = 0
    i=1
    while i !=0:
        if x == 0:
                sys.stdout.write("searching.")
                sys.stdout.flush()
                time.sleep(1)
                sys.stdout.write("\r")
                sys.stdout.flush()
                x += 1
        elif x == 1:
                sys.stdout.write("searching..")
                sys.stdout.flush()
                time.sleep(1)
                sys.stdout.write("\r")
                sys.stdout.flush()
                x += 1
        elif x == 2:
                sys.stdout.write("searching...")
                sys.stdout.flush()
                time.sleep(1)
                sys.stdout.write("\r")
                sys.stdout.flush()
                x = 0

def sendmess(a):
    driver.get("https://web.whatsapp.com/")
    driver.implicitly_wait(10)
    driver.find_element_by_xpath("//*[contains(text(), 'Testbot')]").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//*[@title='Taper un message']").send_keys(a)
    driver.find_element_by_class_name("_4sWnG").click()

def tcrnr():
    driver.get("https://www.lnr.fr/rugby-pro-d2/club-rugby/rouen-normandie-rugby-pro-d2")
    try :
        driver.implicitly_wait(4)
        driver.find_element(By.CLASS_NAME,"didomi-continue-without-agreeing").click()
    except :
        pass
    driver.implicitly_wait(2)
    a=driver.find_element(By.CLASS_NAME, 'number').text
    a="Rouen est classé : {}".format(a)
    print(a)
    sendmess(a)

def act(a):
    if a == "stop.":
        i = -1
    if a == "actif?":
        sendmess("Je suis actif ;)")
        date = datetime.datetime.now()
        sec = 60 - date.second
        time.sleep(sec)
    if a == "rnr!":
        tcrnr()
        date = datetime.datetime.now()
        sec = 60 - date.second
        time.sleep(sec)

def search():

    i=0
    while i != -1 :
        driver.implicitly_wait(4)
        try:
            d = "{}".format(datetime.datetime.now())
            date = datetime.datetime.now()
            mm = date.minute
            hh = date.hour
            tim = "[{}:{}, {}/{}/{}]".format(hh, mm, d[8:10], d[5:7], d[0:4])
            in_xpath='//div[@class="copyable-text"][@data-pre-plain-text="{} Pierre-Jean: "]'.format(tim)
            text = driver.find_element_by_xpath(in_xpath).text
            print("\n",text)
            act(text)


        except:
            pass
    print("Exiting program")
    time.sleep(15)
    exit()

def loop():
    class myThread(threading.Thread):
        def __init__(self, threadID, name):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name

        def run(self):
            print("Starting " + self.name)
            if self.threadID==1 :
                search()
            elif self.threadID==2 :
                searching()
            print("\nExiting " + self.name)

    thread1 = myThread(1, "Logger")
    thread2 = myThread(2, "ROBOT")
    try:
        thread1.start()
        thread2.start()

    except:
        print("Error: unable to start thread")


init()
