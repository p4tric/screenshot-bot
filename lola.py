#import from selenium driver
from selenium import webdriver
#import from use of Key actions && Action chains (commands) from selenium driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import pyautogui
from pathlib import Path
home = str(Path.home()) + '/'


lists = ["https://www.111.com", "https://222.com", "https://www.333.com/"]
#designate webdriver as chrome
driver = webdriver.Chrome('./chromedriver')

count = 0
for link in lists:
    count += 1
    print('URL: ' + link + '\nScreenshot located at: ' + home + 'screenshot_' + str(count) + '.png\n\n')
    driver.get(link)
    driver.implicitly_wait(15)
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(home + 'screenshot_' + str(count) + '.png')
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[count])
