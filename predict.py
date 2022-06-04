import csv
import estimate

def request_data():
	try:
		mileage = int(input('Enter mileage: '))
		if mileage < 0:
			raise ValueError
		return mileage
	except ValueError:
		print('Invalid input!')
		return request_data()

print('Loading data...')

with open('result.csv', 'r') as file:
	reader = csv.reader(file)
	header = next(reader)
	theta = [float(x) for x in next(reader)]
	file.close()

mileage = request_data()
price = estimate.price(mileage, theta)
print('Price:', price)