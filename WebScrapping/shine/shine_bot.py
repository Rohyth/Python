
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

class shineBot():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options);
        
        
    
    def login(self):
        self.driver.get("https://recruiter.shine.com/")
        sleep(2)
        try:
            self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
        except:
            pass
        
        self.driver.find_element_by_xpath('//*[@id="id_myDropdown"]/form/ul/li[1]/input').send_keys('basicsofimmigrationc')
        self.driver.find_element_by_xpath('//*[@id="id_myDropdown"]/form/ul/li[2]/input').send_keys('Basics#2115')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="id_myDropdown"]/form/ul/li[3]/input').click()
        print('Reached login Page')   
        #059665
        sleep(100)
        
        self.driver.get('https://recruiter.shine.com/myshine/managejobs')
        self.driver.find_element_by_xpath('//*[@id="i1d_main_wrap"]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[1]/form/ul/li[4]/input').send_keys('04/02/2020')        
        self.driver.find_element_by_xpath('//*[@id="i1d_main_wrap"]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[1]/form/ul/li[6]/input').send_keys('04/30/2020')
        self.driver.find_element_by_xpath('//*[@id="i1d_main_wrap"]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[1]/form/ul/li[8]/input').click()
        sleep(2)
        print('Entered login credentials')
        
        #Master Loop starts here
        tot = self.driver.find_element_by_xpath('//*[@id="i1d_main_wrap"]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/ul/li[1]').get_attribute('innerHTML')
        Ftot = tot.replace('1 of ','')
        
        resultset = self.driver.find_element_by_xpath('//*[@id="i1d_main_wrap"]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul')
        xopt = resultset.find_elements_by_tag_name('li')        
        for opt in xopt:
            print(opt.text)
        
        