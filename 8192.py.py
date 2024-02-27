# import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time
from bs4 import BeautifulSoup
import numpy as np
from play import step, game

_time = random.randint(5,7)



# sl = 16


# phase = []
# with open('file_phase.txt', 'r', encoding='utf-8') as file:
#     words = file.readlines()
#     for line in words:
#         line = line.strip()
#         phase.append(line)
# phase_split = np.array_split(phase,sl)

key = ''
key_list = key.split()[:12]


EXTENSION_PATH = "C:\\Users\\vinhthomxoai\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\mcbigmjiafegjnnogedioegffbooigli\\1.0.1.8_0.crx"

options = webdriver.ChromeOptions()
options.add_argument('window-size=750,1000')
options.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(options = options)
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)   
while True:
    try: 
        driver.find_element(By.XPATH, ('/html/body/div/div/div/div[2]/div[2]/a[3]/div[1]')).click()
        break
    except:
        pass
time.sleep(1)
driver.find_element(By.ID, 'word-0').send_keys(key_list[0])
driver.find_element(By.ID, 'word-1').send_keys(key_list[1])
driver.find_element(By.ID, 'word-2').send_keys(key_list[2])
driver.find_element(By.ID, 'word-3').send_keys(key_list[3])
driver.find_element(By.ID, 'word-4').send_keys(key_list[4])
driver.find_element(By.ID, 'word-5').send_keys(key_list[5])
driver.find_element(By.ID, 'word-6').send_keys(key_list[6])
driver.find_element(By.ID, 'word-7').send_keys(key_list[7])
driver.find_element(By.ID, 'word-8').send_keys(key_list[8])
driver.find_element(By.ID, 'word-9').send_keys(key_list[9])
driver.find_element(By.ID, 'word-10').send_keys(key_list[10])
driver.find_element(By.ID, 'word-11').send_keys(key_list[11])



time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/form/div[2]/div/button/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div[3]/div/a/button/span').click()
time.sleep(2)
driver.find_element(By.ID, 'password').send_keys('Abcdxyz123!')
driver.find_element(By.ID, 'confirmPassword').send_keys('Abcdxyz123!')
driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div[2]/form/div[2]/input').click()
driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[1]/div[2]/form/div[3]/div/button/span').click()
time.sleep(3)

driver.get('https://sui8192.ethoswallet.xyz/')
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/div[1]/div[1]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[3]/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/button/div').click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[2]/button/span').click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])

while True:
	try: 
		driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[3]/div[3]/div[1]/div[7]/div/div[1]').click()
		break
	except:
		pass

time.sleep(5)

driver.switch_to.window(driver.window_handles[-1])
while True:
	try: 
		driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[2]/button').click()
		break
	except:
		pass

time.sleep(5)





def _matrix(xpath):
    element = driver.find_element(By.XPATH, xpath)
    source_code = element.get_attribute("innerHTML")
    soup = BeautifulSoup(source_code, 'html.parser')

    matrix = np.zeros((4, 4), dtype=int)
    rows = soup.find_all(class_=lambda x: x and x.startswith("row-"))

    for i, row in enumerate(rows):
        tiles = row.find_all(class_="tile-wrapper")
        for j, tile in enumerate(tiles):
            value = tile.find(class_="value")
            if value:
                matrix[i][j] = int(value.get_text())

    return matrix

def _cfpass(_password):
	_password.send_keys('Abcdxyz123!')
	driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[3]/form/div/div[2]/button/span').click()




driver.switch_to.window(driver.window_handles[1])

while True:
	bd = driver.find_element(By.TAG_NAME, "html")
	matrix = _matrix('/html/body/div[1]/div[5]/div/div[7]')
	print(matrix)
	num_rows = len(matrix)
	num_cols = len(matrix[0])

	if driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[3]/div[3]/button[2]').is_displayed():
	    driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[3]/div[3]/button[2]').click()
	    time.sleep(10)
	    driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/div/div[3]/div[3]/div[1]/div[1]/div[2]/button').click()
	    time.sleep(2)
	    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[7]/div[2]/button').click()
	    time.sleep(3)

	    while True:
	        try:
	            driver.switch_to.window(driver.window_handles[-1])
	            driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[3]/div[2]/button').click()
	            break
	        except:
	            pass
	    time.sleep(10)

	    while True:
	        try:
	            driver.switch_to.window(driver.window_handles[-1])
	            driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[2]/button/span').click()
	            break
	        except:
	            pass
	    time.sleep(10)

	try:
		driver.switch_to.window(driver.window_handles[-1])
		time.sleep(5)
		if driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[2]/button/span').is_displayed():
			time.sleep(_time)
			driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[2]/button/span').click()
		elif driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[2]/button/span').is_displayed():
			time.sleep(_time)
			driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[2]/button/span').click()
		elif driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[3]/form/div/div[1]/div/input').is_displayed():
			time.sleep(_time)
			driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[3]/form/div/div[1]/div/input').send_keys('Abcdxyz123!')
			driver.find_element(By.XPATH, '/html/body/div/div/div/div/div[3]/form/div/div[2]/button/span').click()
			time.sleep(3)
		# break
	except:
		pass


	driver.switch_to.window(driver.window_handles[1])
	step().run_step0(matrix, num_rows, num_cols, driver)
	time.sleep(_time)


