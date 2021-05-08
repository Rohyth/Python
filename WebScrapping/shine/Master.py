from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import pandas as pd
from time  import sleep

'opts = Options() ,opts.set_headless()'

browser = webdriver.Firefox(executable_path='/home/rohyth/Python/WebScrapping/geckodriver')
browser.get('https://recruiter.shine.com/')

login = browser.find_element_by_xpath('//*[@id="loginbutton"]').click()
usr = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[1]/input').send_keys('basicsofimmigrationc')
pwd = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[2]/input').send_keys('Basics#2115')

pressLogin = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div[1]/div/div/form/ul/li[3]/input').click()


Otp = browser.find_element_by_xpath('//*[@id="id_userOtp"]').send_keys('268814')
sub = browser.find_element_by_xpath('//*[@id="id_otpSubmit"]').click()

browser.get('https://recruiter.shine.com/myshine/managejobs')
sleep(5)
Base = {
        'Category':[],
        'link':[],
        'status':[]
        }

df = pd.DataFrame(Base)

#Total_li = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]')

Page_count = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/ul/li[1]').get_attribute('innerHTML')
Page_count = int(Page_count.split(' ')[2])

for y in range(0,Page_count):
    print('Page ', y )
    
    #new code-------------------------------
    
    
    #----------------------------------------
    for x in range(2,12):
        C = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul/li['+ str(x) +']/span[2]/a').get_attribute('innerHTML')
        L = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul/li['+ str(x) +']/span[3]/span/span[1]/a').get_attribute('href')
                
        if x ==11:
            S = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul/li['+ str(x) +']/span[4]/span[1]/span/span[1]').get_attribute('innerHTML')
        else:
            S = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul/li['+ str(x) +']/span[4]/span[1]/span').get_attribute('innerHTML')
        
        if str(S) == 'Published':
           df = df.append({'Category':C,'link':L, 'status':S}, ignore_index=True)
    
    browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/ul/li[3]/a').click()
    sleep(5)
    
    N_Page_count = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/ul/li[1]').get_attribute('innerHTML')
    N_Page_count = int(N_Page_count.split(' ')[0])
    
    if (x-1) == N_Page_count:
        sleep(5)
  

ul = browser.find_element_by_xpath('/html/body/div[2]/div[2]/app/div/app-managejobs/div/div[2]/div[2]/div/div[2]/ul')
li =  ul.find_elements_by_tag_name('li')

for l in li:
    if 'Published' in str(l.text):
        print(l.get_attribute('href'))

m_li = [l for l in li if 'Published' in str(l.text)]

links = li.find_elements_by_tag_name('a')
status = li.find_elements_by_tag_name('span')

C = [v.get_attribute('innerHTML') for v in links if 'manage-jobs' in str(v.get_attribute('href'))]  
L = [v.get_attribute('href') for v in links if 'sapplicants' in str(v.get_attribute('href'))]
S = [v.get_attribute('innerHTML') for v in status]

        
    
# Master loop


t_url = df['link'][0]

browser.get(t_url)
browser.find_element_by_xpath('/html/body/div[3]/div[3]/div[1]/div[2]/div[2]/div/div[3]/div[2]/div[1]/div/div[1]/div[1]/div[2]/div/a').click()


for ind in df.index:
    t_url = df['link'][ind]
    t_Cat = df['Category'][ind]
    
    
    