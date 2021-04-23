from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from login import turnOffMicCam, AskToJoin, Glogin, joinNow
from attendance import attendance
from attendanceform import attendanceForm
# from createpdf import createpdf
from randomstudent import randomStudent
from newword import newWord
from quotes import quote
#from screenshots import ss
from foullang import foulLanguage

# ADD CREDENTIALS HERE
CREDS = {'email': 'gmeetassistishere@gmail.com', 'passwd': 'LetsGetPumping4now'}

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--mute-audio")
opt.add_argument("start-maximized")
opt.add_argument("enable-usermedia-screen-capturing")
opt.add_experimental_option('excludeSwitches', ['test-type'])
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe",options=opt)
print("browser up")


def commands():
    i = 1
    key = 1
    j = 1
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span').click()
    mom = []
    students = []
    flag=true
    # infinite loop
    while (key == 1):
        if(flag==true):
            WebDriverWait(driver, 100000).until(EC.visibility_of_element_located((By.XPATH,
                                                                                '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[' + str(
                                                                                    i) + ']/div[2]/div[' + str(j) + ']')))
            print('1. value of i is', i)
            print('1. value of j is', j)
            instText = driver.find_element_by_xpath(
                '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[' + str(
                    i) + ']/div[2]/div[' + str(j) + ']').text
        if(flag==false):
            while(key==1):
                try:
                    i=i+1
                    j=1
                    WebDriverWait(driver, 100000).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[' + str(
                                                                                              i) + ']/div[2]/div[' + str(
                                                                                              j) + ']')))
                    elem = driver.find_element_by_xpath(
                        '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[' + str(
                            i + 1) + ']/div[1]/div[1]')
                except NoSuchElementException:
                    pass
                try:
                    j=j+1
                    WebDriverWait(driver, 100000).until(EC.visibility_of_element_located((By.XPATH,
                                                                                          '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[' + str(
                                                                                              i) + ']/div[2]/div[' + str(
                                                                                              j) + ']')))
                    elem = driver.find_element_by_xpath(
                        '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[2]/div[' + str(
                            i + 1) + ']/div[1]/div[1]')
                except NoSuchElementException:
                    pass

        instText = str(instText).lower()

        # foul language
        if (foulLanguage(instText)):
            driver.find_element_by_xpath(
                '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(
                "Please don't make use of inappropriate language." + Keys.ENTER)
            i = i + 2
            j = 1
            flag=true
        # all tags
        elif (instText == '/attendance'):
            students = attendance(driver)
            i = i + 2
            j = 1
            print(' Attendance printed', i, j)
            flag = true
        elif (instText == '/attendanceform'):
            attendanceForm(driver)
            i = i + 2
            j = 1
            print(' attendanceform printed', i, j)
            flag = true
        elif (instText.startswith('m/')):
            mom.append(instText[4:])
            driver.find_element_by_xpath(
                '//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(
                'Updated' + Keys.ENTER)
            i = i + 2
            j = 1
            print(' mom created', i, j)
            flag = true
        elif (instText.find('/random') != -1):
            randomStudent(driver)
            i = i + 2
            j = 1
            print(' random printed', i, j)
        elif (instText == '/quote'):
            quote(driver)
            i = i + 2
            j = 1
            flag = true
            print(' quote printed', i, j)
        elif (instText == '/newword'):
            newWord(driver)
            i = i + 2
            j = 1
            flag = true
            print(' newword printed', i, j)
        elif (instText == '/ss'):
            ss(driver)
            i = i + 2
            j = 1
            flag = true
            print('Screenshot taken', i, j)
        elif (instText == '/exit'):
            key = 0
            createpdf(students, mom)
            i = i + 2
            j = 1
            flag = true
            print('mom printed and exit', i, j)
        else:
            flag=false



# login
Glogin(CREDS['email'], CREDS['passwd'], driver)
driver.get("https://meet.google.com/ruw-jhcm-szo")
time.sleep(5)
turnOffMicCam(driver)
driver.implicitly_wait(15)
joinNow(driver)
driver.implicitly_wait(10)
time.sleep(5)
commands()