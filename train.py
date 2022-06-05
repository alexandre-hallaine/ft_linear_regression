import csv
import estimate

import plotly.graph_objects as go


def normalisation(data):
    return [(row - min(data)) / (max(data) - min(data)) for row in data]


def train(data, theta, learning_rate):
    sum = [0, 0]
    for i in range(len(data[0])):
        x, y = [row[i] for row in data]
        estimated_y = estimate.price(x, theta)
        sum[0] += (estimated_y - y)
        sum[1] += (estimated_y - y) * x
    return [theta[i] - learning_rate * sum[i] / len(data[i]) for i in range(len(theta))]


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

print('Training...')

theta = [1, 1]
learning_rate = 1
print('Learning rate:', learning_rate)

while True:
    new = train([normalisation(mileages), normalisation(prices)],
                theta, learning_rate)
    if new == theta:
        break
    theta = new
    print('Theta Normalised:', theta, end='\r')
print()

deltaX = max(mileages) - min(mileages)
deltaY = max(prices) - min(prices)
theta[1] = deltaY * theta[1] / deltaX
theta[0] = ((deltaY * theta[0]) + min(prices) - theta[1]
            * (deltaY / deltaX) * min(mileages))
print('Theta Denormalised:', theta)

print('Writing result...')

with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['theta_0', 'theta_1'])
    writer.writerow(theta)
    file.close()

print('Done!')

x = [min(mileages), max(mileages)]
y = [estimate.price(x, theta) for x in x]

fig = go.Figure()
fig.update_layout(xaxis_title='Mileage', yaxis_title='Price')
fig.add_trace(go.Scatter(x=mileages,
              y=prices, mode='markers', name='Data'))
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Estimate'))
fig.show()
