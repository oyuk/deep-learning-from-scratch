import sys,os
import numpy as np
sys.path.append(os.pardir)
import pickle
from deep_learning_from_scratch.dataset.mnist import load_mnist
from deep_learning_from_scratch.common.functions import sigmoid, softmax


(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True,one_hot_label=True)
print(x_train.shape)
print(t_train.shape)
