import time
from selenium.webdriver.common.keys import Keys

students=[]
def attendance(driver):
    print(2)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[1]/span/span').click()
    time.sleep(5)
    attendance=driver.find_element_by_class_name('GvcuGe').text
    students=attendance.split('\n')
    students.remove('gmeet helper')
    students.remove('(You)')
    if 'Presentation' in students:
        students.remove('Presentation')
    print(students)
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[1]/div[2]').click()
    driver.implicitly_wait(2000)
    return(students)
