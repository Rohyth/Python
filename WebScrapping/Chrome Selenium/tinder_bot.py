from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = webdriver.ChromeOptions(); 
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options);  
        
        
    def login(self):
        self.driver.get("http://www.tinder.com")
        sleep(5)
        
        try:
            self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
        except:
            pass
        
        try:
            self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/button').click()
        except:
            pass
        
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/button').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[3]/button').click()
        Inum = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input')
        Inum.send_keys('7290845646')
        lbtn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        lbtn.click()
        
        
                