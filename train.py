import csv
import estimate

import plotly.graph_objects as go


def infinity():
    i = 0
    while True:
        yield i
        i += 1


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

theta = [0, 0]
learning_rate = 0.1
normalised_mileages = normalisation(mileages)
normalised_prices = normalisation(prices)

trained_figure = go.Figure()
trained_figure.update_layout(
    xaxis_title='Mileage', yaxis_title='Price', title='Training')
trained_figure.add_trace(go.Scatter(x=normalised_mileages,
                                    y=normalised_prices, mode='markers', name='Data'))

print('Learning rate:', learning_rate)
for i in infinity():
    new = train([normalised_mileages, normalised_prices],
                theta, learning_rate)
    if new == theta:
        break
    theta = new
    print('Theta Normalised:', theta, end='\r')

    if i % int(1 / learning_rate) != 0:
        continue

    x = [min(normalised_mileages), max(normalised_mileages)]
    y = [estimate.price(x, theta) for x in x]
    trained_figure.add_trace(go.Scatter(x=x, y=y, mode='lines',
                             name='Estimate {}'.format(i)))
print()

delta = [max(x) - min(x) for x in [mileages, prices]]
theta[1] = theta[1] * delta[1] / delta[0]
theta[0] = theta[0] * delta[1] + min(prices) - theta[1] * min(mileages)
print('Theta Denormalised:', theta)

x = [min(mileages), max(mileages)]
y = [estimate.price(x, theta) for x in x]

denormalised_figure = go.Figure()
denormalised_figure.update_layout(xaxis_title='Mileage', yaxis_title='Price')
denormalised_figure.add_trace(go.Scatter(x=mileages,
                                         y=prices, mode='markers', name='Data'))
denormalised_figure.add_trace(go.Scatter(
    x=x, y=y, mode='lines', name='Estimate'))

print('Writing result...')

with open('result.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['theta_0', 'theta_1'])
    writer.writerow(theta)
    file.close()

print('Done!')

trained_figure.show()
denormalised_figure.show()
