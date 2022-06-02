import os.path

def predict(mileage):
	a, b = 0, 0
	if os.path.isfile("result"):
		with open("result", "r") as f:
			lines = f.readlines()
			f.close()
			try:
				if (len(lines) != 2):
					raise ValueError
				a, b = [int(x) for x in lines]
			except ValueError:
				print("The result file is corrupted.")
				print("Please try again.")
				exit(1)
	return a * mileage + b

def request():
	try:
		mileage = int(input("Enter the mileage of the car: "))
		if mileage < 0:
			raise ValueError
		print("The  price of the car is", predict(mileage) / 100, "dollars")
	except ValueError:
		print("The mileage must be a positive integer.")
		print("Please try again.")
		request()
request()