import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('california_housing_test.csv')

'''def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].housing_median_age
        y = points.iloc[i].score
        total_error += (y - (m * x * b)) ** 2
    total_error / float(len(points))


'''

def gradient_descent(m_now, b_now, points, L):
    #L is the learning rate
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].median_house_value
        y = points.iloc[i].median_income

    m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
    b_gradient += -(2/n) * (y - (m_now * x + b_now))
    # encountering an overflow with the scalar multiply function. need to be more efficient and easy on the system I think

    m = m_now - (m_gradient * L)
    b = m_now - (b_gradient * L)
    #giving me an invalid value because the math in the gradient variables is causing overflow
    #which is causing difficulties in calculating the values of m_gradient and b_gradient
    return m, b


m = 0
b = 0
L = 0.0001

epochs = 100


for i in range(epochs):
    if i % 50 == 0:
        print(f"Epoch: {i}")
    m, b = gradient_descent(m, b, data, L)

print(m, b)

plt.scatter(data.median_income, data.median_house_value, color = "black")
plt.plot(list(range(1000, 2500)), [m * x * b for x in range(1000, 2500)], color = "red")
plt.show()


