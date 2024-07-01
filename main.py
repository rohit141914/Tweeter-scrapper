from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests

url='https://www.x.com/i/flow/login'
user=''
passd=""
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(3)
# driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div[2]/div/div/div/button/div').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a/div/span').click()
# time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input').send_keys(user)
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(passd)
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span' ).click()
time.sleep(10)

a=driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/section').text
# print(a)
# make an list of all the elements in the section
b=a.split('\n')
print(b)

# filtered_list = []
# for string in b:
#  if string.startswith('#'):
#   filtered_list.append(string)
# print(filtered_list) 


def remove_trending_with_strings(b):
    return [s for s in b if 'Trending with' not in s]

b = remove_trending_with_strings(b)

result = []
prev_string = None
    
for curr_string in b:
        if prev_string and 'Trending' in prev_string:
            result.append(curr_string)
        prev_string = curr_string
    
result.pop(0)    
print(result)
time.sleep(5)