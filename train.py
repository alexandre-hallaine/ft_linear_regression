import csv
import estimate

def normalisation(data):
	return [(row - min(data)) / (max(data) - min(data)) for row in data]

def train(data, theta, learning_rate):
	sum = [0, 0]
	for i in range(len(data[0])):
		x, y = [row[i] for row in data]
		estimated_y = estimate.price(x, theta)
		sum[0] += (estimated_y - y)
		sum[1] += (estimated_y - y) * x
	return [learning_rate * sum[i] / len(data[i]) for i in range(len(theta))]

print('Loading data...')

mileages = []
prices = []
with open('data.csv', 'r') as file:
	reader = csv.reader(file)
	header = next(reader)
	for row in reader:
		mileages.append(int(row[0]))
		prices.append(int(row[1]))
	file.close()
normalised = [normalisation(mileages), normalisation(prices)]

print('Training...')

theta = [1, 1]
while True:
	new = train(normalised, theta, 0.1)
	if (new == theta):
		break
	theta = new

#need to denormalise theta

print('Writing result...')

with open('result.csv', 'w') as file:
	writer = csv.writer(file)
	writer.writerow(['theta_0', 'theta_1'])
	writer.writerow(theta)
	file.close()

print('Done!')