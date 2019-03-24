import numpy as np
from numerical_gradient import numerical_gradient
from function_2 import function_2

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x

    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x    

init_x = np.array([-3.0, 4.0])
a = gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100)
print(a)
