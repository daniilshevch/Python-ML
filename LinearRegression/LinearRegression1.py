import numpy as np
production_hours = np.array([34,35,39,42,43,47])
production_volume = np.array([102,109,137,148,150,158])
x_average = production_hours.mean()
y_average = production_volume.mean()
print(x_average)
print(y_average)
x_minus_x_average = production_hours - x_average
y_minus_y_average = production_volume - y_average
print(x_minus_x_average)
print(y_minus_y_average)
x_minus_x_average_multiply_y_minus_y_average = x_minus_x_average * y_minus_y_average
print(x_minus_x_average_multiply_y_minus_y_average)
sum_of_x_minus_x_average_multiply_y_minus_y_average = x_minus_x_average_multiply_y_minus_y_average.sum()
x_minus_x_average_squared = x_minus_x_average * x_minus_x_average
print(sum_of_x_minus_x_average_multiply_y_minus_y_average)
print(x_minus_x_average_squared)
sum_of_x_minus_x_average_squared = x_minus_x_average_squared.sum()
print(sum_of_x_minus_x_average_squared)
b1 = sum_of_x_minus_x_average_multiply_y_minus_y_average / sum_of_x_minus_x_average_squared
print(b1)
b0 = y_average - b1 * x_average
print(b0)
