from selenium.webdriver.common.keys import Keys

def attendanceForm(driver):
    driver.implicitly_wait(5)
    driver.execute_script("window.open('https://docs.google.com/forms/u/0/')")
    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(20)
    driver.find_element_by_id(':1g').click()
    driver.find_element_by_xpath('//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[4]').click()
    driver.find_element_by_xpath('//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]/span').click()
    driver.find_element_by_xpath('//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span/div/div/div[1]/div[2]/textarea').send_keys('Enter student name: ')
    driver.find_element_by_xpath('//*[@id="SchemaEditor"]/div/div[1]/div/div/div[1]/div/span/span/div').click()
    driver.find_element_by_xpath('//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[1]/div[1]/div[4]').click()
    driver.find_element_by_xpath('//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]/span').click()
    driver.find_element_by_xpath('//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[3]/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span/div/div/div[1]/div[2]/textarea').send_keys('Enter your school registration number: ')
    driver.find_element_by_xpath('//*[@id="SchemaEditor"]/div/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/div/span/div/div[1]/div[2]/textarea').send_keys('Attendance form')
    driver.find_element_by_xpath('//*[@id="tJHJj"]/div[1]/div[2]/div/div[5]/div/span/span').click()
    driver.find_element_by_xpath('//*[@id="VVcGtd"]/div[1]/div[3]/span').click()
    driver.find_element_by_xpath('//*[@id="link"]/div/div/div[4]/div[2]/span/span').click()
    driver.implicitly_wait(5)
    driver.close()
    #driver.find_element_by_css_selector('body').send_keys(Keys.CONTROL+'w')
    driver.switch_to.window(driver.window_handles[0])
    #driver.find_element_by_xpath('// *[ @ id = "ow3"] / div[1] / div / div[9] / div[3] / div[1] / div[3] / div / div[2] / div[3] / span / span').click()
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(Keys.CONTROL+'v')

    # driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[2]/span/span/span/svg').click()
    driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(Keys.ENTER)