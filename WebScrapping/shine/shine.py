from selenium.webdriver.firefox.options import Options
from selenium import webdriver

'opts = Options() ,opts.set_headless()'

browser = webdriver.Firefox(executable_path='/usr/bin/geckodriver')
browser.get('https://recruiter.shine.com/')

login = browser.find_element_by_xpath('//*[@id="loginbutton"]').click()
usr = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[1]/input').send_keys('basicsofimmigrationc')
pwd = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[2]/input').send_keys('Basics#2115')

pressLogin = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[3]/input').click()

Otp = browser.find_element_by_xpath('//*[@id="id_userOtp"]').send_keys('264260')
sub = browser.find_element_by_xpath('//*[@id="id_otpSubmit"]').click()

browser.get('https://recruiter.shine.com/myshine/managejobs')

