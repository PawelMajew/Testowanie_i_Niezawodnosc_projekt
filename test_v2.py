import serial
import random
import time
import math
import numpy as np

def funKwadratowa():
	print("\n=========quadratic function=============")
	FAIL = 0

	zero1_out = 1
	zero2_out = 1
	coefficients_list = []
	max_number = 255
	for a in range(1, max_number):
		for b in range(1, max_number):
			for c in range(1, max_number):
				coefficients_list.append((a, b, c))	

	for num in coefficients_list:
		a, b, c = num
		print("Fun: (" + str(a)+ ")x^2 + (" + str(b) + ")x + (" + str(c) + ")")

		time.sleep(2)
		ser.write(bytes(str(c) + " " + str(b) + " " + str(a) + "\n", 'utf-8'))

		while True:
			if ser.in_waiting > 0:
				result = ser.readline().decode('utf-8').rstrip() #reading the result from the serial port
				numbers = result.split(" ")
				num_count = len(numbers)
				#saves the data received into variables
				if numbers[0] != 'NULL':
					numbers[0] = float(numbers[0])
					if num_count == 2:
						numbers[1] = float(numbers[1])
					print("Output: " +  str(numbers))
					break
				else:
					print("Output: " +  str(numbers[0]))
					break


		coefficients = np.array([a, b, c])

		#calculation of zeros
		roots = np.roots(coefficients)
		if np.iscomplexobj(roots[0]):
			roots = 'NULL'
			print("Correct value: " + str(roots))
			if numbers[0] == 'NULL':
				print("PASS\n")
			else:
				print("FAIL\n")
				FAIL = 1
		elif roots[0] == 0.0 and roots[1] == 0.0:
			roots = 0.0
			print("Correct value: " + str(roots))
			if numbers[0] == roots:
				print("PASS\n")
			else:
				print("FAIL\n")
				FAIL = 1
		elif len(numbers) == 1:
			roots[0] = round(roots[0],2)
			print("Correct value: " + str(roots[0]))
			if roots[0] == numbers[0]:
				print("PASS\n")
			else:
				print("FAIL\n")
				FAIL = 1
		else:
			roots[0] = round(roots[0],2)
			roots[1] = round(roots[1],2)
			#sorting list
			roots = sorted(roots)
			numbers = sorted(numbers)
			print("Correct value: " + str(numbers))
			if roots == numbers:
				print("PASS\n")
			else:
				print("FAIL\n")
				FAIL = 1

	print("\n---test for quadratic function end---")
	if FAIL == 0:
		print("test successful")
	else:
		print("test fail")


def funLiniowa():
	print("\n=========linear function=============")
	FAIL = 0

	coefficients_list = []
	max_number = 255
	for b in range(1, max_number):
		for c in range(1, max_number):
			coefficients_list.append((b, c))	

	zero_out = 1 #output from serial

	for num in coefficients_list:
		a, b = num

		print("Fun: (" + str(b) + ")x + (" + str(c) + ")")

		time.sleep(2)
		ser.write(bytes(str(c) + " " + str(b) + " " + "\n", 'utf-8'))

		while True:
			if ser.in_waiting > 0:
				result = ser.readline().decode('utf-8').rstrip() #reading the result from the serial port
				#saves the data received into variables
				zero_out = float(result)
				break
		print("Output: " +  str(zero_out))

		coefficients = np.array([0, b, c])

		#calculation of zeros
		roots = np.roots(coefficients)
		roots[0] = round(roots[0],2)
		print("Correct value: " + str(roots[0]))

		if zero_out == roots:
			print("PASS")
		else:
			print("FAIL")
			FAIL = 1
	print("\n---test for linear function end---")
	if FAIL == 0:
		print("test successful")
	else:
		print("test fail")


if __name__ == "__main__":

	ser = serial.Serial('COM3', 9600) #serial port initialization, change 'COM3' to the appropriate port used by Arduino
	print("/// start tests ///")
	funKwadratowa()
	funLiniowa()
	ser.close() #close the serial port
