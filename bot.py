
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#time to refresh page
#Timer = random.randrange(180,185)
#180 #(3 min)

#number of views
views = 1000000

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located

# Navigate to url with video being appended to search_query
# driver.get("https://www.youtube.com/results?search_query=" + str('crayfish+afternoon+grooming'))
# driver.get("https://www.zambido.com:8960/creativ-space-kitchen/");

# play the video
#wait.until(visible((By.ID, "video-title")))
#driver.find_element_by_id("video-title").click()

"""
wait.until(visible((By.ID, "23")))
driver.find_element_by_id("23").click()

for i in range(views):
    # Timer = random.randrange(180, 190, 2)
    Timer = random.randrange(120, 130, 2)
    print(Timer)
    time.sleep(Timer)
    driver.refresh()
"""
















"""
import time
from selenium import webdriver

#youtube link
link = 'https://youtu.be/AfzjwfW_HW4'

#time to refresh page
Timer = 180 #(3 seconds)
#number of views
views = 10

driver = webdriver.Chrome('./chromedriver')
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()
"""
