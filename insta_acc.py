''' Developed by Atharva Srivastava
Pull requests are welcome.'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime

chromedriver_path = 'D:\\chromedriver.exe'                          # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

# Please enter your username and password in the below ####

username = webdriver.find_element_by_name('username')
username.send_keys('########')
password = webdriver.find_element_by_name('password')
password.send_keys('########')
sleep(1)
button_login = webdriver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div/div[3]/button').click()
sleep(3)


#comment these last 2 lines out, if you don't get a pop up asking about notifications
notnow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notnow.click() 

search_bar = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys('atharva')
sleep(1)
# search_bar_click = webdriver.find_element_by_xpath(
#     '//*[@id = "react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span').click()
search_bar.send_keys(Keys.DOWN)
sleep(1)
search_bar.send_keys(Keys.RETURN)
#search_bar.send_keys(Keys.RETURN)
sleep(4)

'''Can be used for following'''

# follow_button_private_1 = webdriver.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/header/section/div[2]/button').click()

# follow_button_private_2 = webdriver.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/header/section/div[1]/button').click()

# follow_button_open_1 = webdriver.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').click()

# follow_button_open_2 = webdriver.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/header/section/div[2]/div[1]/span/span[1]/button').click()


#open_photo = webdriver.find_element_by_xpath(
 #   '//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div[1]/div[2]').click()

# total_followers = webdriver.find_element_by_xpath(
#     '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text

# print(total_followers)

open_photo = webdriver.find_element_by_xpath(
    '/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div[1]/div[2]').click()

sleep(1)

like_button = webdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()

parse_right_initial = webdriver.find_element_by_xpath(
    '/html/body/div[5]/div[1]/div/div/a').click()

sleep(1)

for i in range(0,50):

    like_button = webdriver.find_element_by_xpath(
        '/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()

    parse_right_final = webdriver.find_element_by_xpath(
        '/html/body/div[5]/div[1]/div/div/a[2]').click()

    sleep(1)

    print('Liked',i+1,'photo')

# parse_right_final = webdriver.find_element_by_xpath(
#     '/html/body/div[4]/div[1]/div/div/a[2]').click()
