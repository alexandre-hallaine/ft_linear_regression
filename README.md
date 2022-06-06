# ft_linear_regression

The first AI project of 42. It aims to introduce us to machine learning by implementing gradient descent.

From a set of data, we must use any language to calculate several numbers that will allow us to make a calculation in order to have the value of a car.

# Usage

- First run the training (for the prediction to work):
```bash
$ python3 train.py
```

- Then just run the prediction and enter your mileage:
```bash
$ python3 predict.py
Loading data...
Enter mileage: <number>
```
> If your value is incorrect you should get the `Invalid input!` error and you will be asked for the mileage again.


- You now have the price of the car
```bash
Price: 8000
```

# Explanation
- The values are first normalized (scaled between 0 and 1) to be easier to process.
- Normalized thetas are then calculated via gradient descent
![Training](/images/training.png)

- A denormalized version of thetas is calculated so that it can be used with normal values.
![Data](/images/data.png)

- We can now predict the price of a car with an affine function (with thetas), and voila
