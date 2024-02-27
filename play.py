import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class game():

	def __init__(self):
		pass

	def move_down(self, driver):
		bd = driver.find_element(By.TAG_NAME, "html")	
		bd.send_keys(Keys.ARROW_DOWN)
		print('move_down')

	def move_left(self, driver):
		bd = driver.find_element(By.TAG_NAME, "html")	
		bd.send_keys(Keys.ARROW_LEFT)
		print('move_left')

	def move_right(self, driver):
		bd = driver.find_element(By.TAG_NAME, "html")	
		bd.send_keys(Keys.ARROW_RIGHT)
		print('move_right')



class step():

	
	def __init__(self):
		pass


	def run_step0(self, matrix, num_rows, num_cols, driver):
	        if matrix[3][0] == 0:
	            game().move_left(driver)
	            time.sleep(7)
	            game().move_down(driver)
	            return

	        elif matrix[3][0] == matrix[3][1] or matrix[3][1] == matrix[3][2] or matrix[3][2] == matrix[3][3]:
	            game().move_left(driver)
	            return

	        step().run_step1(matrix, num_rows, num_cols, driver)



	def run_step1(self, matrix, num_rows, num_cols, driver):

		score_col1 = 0
		score_col2 = 0
		score_col3 = 0

		score_row1 = 0
		score_row2 = 0
		score_row3 = 0

		for col in range(len(matrix[0])):
		    if matrix[0][col] == matrix[3][col] and matrix[1][col] == 0 and matrix[2][col] == 0:
		    	score_col3 += matrix[0][col] + matrix[3][col]

		    for row in range(len(matrix) - 1):
		        current_value = matrix[row][col]
		        next_value = matrix[row + 1][col]

		        if current_value == next_value:
		            pair_product = 2 * current_value
		            score_col1 += pair_product

		    for row in range(num_rows - 1):
		        if row < num_rows - 2 and matrix[row][col] == matrix[row+2][col] and matrix[row+1][col] == 0:
		        	score_col2 += matrix[row][col] + matrix[row+2][col]

		_score_col = score_col1+score_col2 + score_col3


		for row in range(len(matrix)):
		    if matrix[row][0] == matrix[row][3] and matrix[row][1] == 0 and matrix[row][2] == 0:
		        score_row1 += matrix[row][0] + matrix[row][3]

		    for col in range(len(matrix[0]) - 1):
		        current_value = matrix[row][col]
		        next_value = matrix[row][col + 1]

		        if current_value == next_value:
		            pair_product = 2 * current_value
		            score_row2 += pair_product

		    for col in range(len(matrix[0])):
		        if col < len(matrix[0]) - 2 and matrix[row][col] == matrix[row][col + 2] and matrix[row][col + 1] == 0:
		            score_row3 += matrix[row][col] + matrix[row][col + 2]

		_score_row = score_row1 + score_row2 + score_row3 


		if _score_col >= _score_row and _score_col >=36:
			game().move_down(driver)
			return
		elif _score_row >= 36:
			game().move_left(driver)
			return
		
		step().run_step2(matrix, num_rows, num_cols, driver)



	def run_step2(self, matrix, num_rows, num_cols, driver):
	    for col in range(num_cols):
	        if matrix[0][col] == matrix[3][col] and matrix[1][col] == 0 and matrix[2][col] == 0 and matrix[0][col] != 0 :
	            game().move_down(driver)
	            return

	        for row in range(num_rows - 1):
	            if matrix[row][col] == matrix[row+1][col] and matrix[row][col] != 0:
	                game().move_down(driver)
	                return

	            elif row < num_rows - 2 and matrix[row][col] == matrix[row+2][col] and matrix[row+1][col] == 0 and matrix[row][col] != 0:
	                game().move_down(driver)
	                return

	    for row in range(num_rows):
	        if matrix[row][0] == matrix[row][3] and matrix[row][1] == 0 and matrix[row][2] == 0 and matrix[row][0] != 0:
	            game().move_left(driver)
	            return

	        for col in range(num_cols - 1):
	            if matrix[row][col] == matrix[row][col+1] and matrix[row][col] != 0:
	                game().move_left(driver)
	                return

	            elif col < num_cols - 2 and matrix[row][col] == matrix[row][col+2] and matrix[row][col+1] == 0:
	                game().move_left(driver)
	                return

	            
	    step().run_step3(matrix, num_rows, num_cols, driver) 
          

	def run_step3(self, matrix, num_rows, num_cols, driver):
	    for col in range(num_cols):
	        if 2*matrix[0][col] == matrix[3][col] and matrix[1][col] == 0 and matrix[2][col] == 0 and matrix[0][col] != 0 :
	            game().move_down(driver)
	            return

	        for row in range(num_rows - 1):
	            if row < num_rows - 2 and 2*matrix[row][col] == matrix[row+2][col] and matrix[row+1][col] == 0 and matrix[row][col] != 0:
	                game().move_down(driver)
	                return

	    for row in range(num_rows):
	        if matrix[row][0] == 2*matrix[row][3] and matrix[row][1] == 0 and matrix[row][2] == 0 and matrix[row][0] != 0:
	            game().move_left(driver)
	            return

	        for col in range(num_cols - 1):
	            if col < num_cols - 2 and matrix[row][col] == 2*matrix[row][col+2] and matrix[row][col+1] == 0:
	                game().move_left(driver)
	                return


	    step().run_step4(matrix, num_rows, num_cols, driver)


	def run_step4(self, matrix, num_rows, num_cols, driver):
	    if 0 in matrix[3]:
	        if any(matrix[3][col] != 0 for col in range(num_cols)):
	            game().move_down(driver)
	            return

	    if 0 not in matrix[3]:
	        if 0 in matrix[2]:
	            game().move_right(driver)
	            return


	    for col in range(num_cols):
	        if matrix[0][col] != 0 and matrix[1][col] == 0 and matrix[2][col] == 0:
	            game().move_down(driver)
	            return

	    for row in range(num_rows):
	        if matrix[row][0] != 0:
	            for col in range(num_cols - 1):
	                if matrix[row][col] == 0 and matrix[row][col+1] != 0:
	                    game().move_down(driver)
	                    return
	            break
	    game().move_right(driver)




