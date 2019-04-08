import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import matplotlib
import scipy.optimize as opt
from sklearn.metrics import classification_report#这个包是评价报告

def load_data(path, transpose=True):
    data = sio.loadmat(path)
    y = data.get('y')  # (5000,1)
    y = y.reshape(y.shape[0])  # make it back to column vector

    X = data.get('X')  # (5000,400)

    if transpose:
        # for this dataset, you need a transpose to get the orientation right
        X = np.array([im.reshape((20, 20)).T for im in X])

        # and I flat the image again to preserve the vector presentation
        X = np.array([im.reshape(400) for im in X])

    return X, y

def expand_y(y):
    res = []
    for i in y:
        y_array = np.zeros(10)
        y_array[i - 1] = 1
        res.append(y_array)
    return np.array(res)

def load_weight(path):
    data = sio.loadmat(path)
    return data['Theta1'], data['Theta2']

def serialize(a, b):
    return np.concatenate((np.ravel(a), np.ravel(b)))

def deserialize(seq):
    return seq[:25 * 401].reshape(25, 401), seq[25 * 401:].reshape(10, 26)

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def feed_forward(theta, X):
    t1, t2 = deserialize(theta)
    m = X.shape[0]
    a1 = X

    z2 = a1@t1.T
    a2 = np.insert(sigmoid(z2), 0, np.ones(m), axis=1)

    z3 = a2@t2.T
    h = sigmoid(z3)

    return a1, z2, a2, z3, h

def cost(theta, X, y):
    m = X.shape[0]
    _,_,_,_,h = feed_forward(theta, X)
    pair_computation = np.multiply(y, np.log(h)) + np.multiply((1-y), np.log(1-h))
    return -pair_computation.sum()/m

def regularized_cost(theta, X , y, l=1):
    t1, t2 = deserialize(theta)
    m = X.shape[0]

    reg_t1 = (l / (2 * m)) * np.power(t1[:, 1:], 2).sum()  # this is how you ignore first col
    reg_t2 = (l / (2 * m)) * np.power(t2[:, 1:], 2).sum()
    return cost(theta, X, y) + reg_t1 + reg_t2

def sigmoid_gradient(z):
    return np.multiply(sigmoid(z), 1-sigmoid(z))

def gradient(theta, X, y):
    t1, t2 = deserialize(theta) #t1:(25,401) t2:(10,26)
    m = X.shape[0]

    delta1 = np.zeros(t1.shape) #(25,401)
    delta2 = np.zeros(t2.shape) #(10,26)

    a1, z2, a2, z3, h = feed_forward(theta, X)

    for i in range(m):
        a1i = a1[i,:] #(1, 401)
        z2i = z2[i,:] #(1, 25)
        a2i = a2[i,:] #(1, 26)

        hi = h[i,:] #(1, 10)
        yi = y[i,:] #(1, 10)

        d3i = hi - yi #(1, 10)

        z2i = np.insert(z2i, 0, np.ones(1)) # make it (1, 26) to compute d2i
        d2i = np.multiply(t2.T @ d3i, sigmoid_gradient(z2i)) #(1, 26)

        delta2 += np.matrix(d3i).T @ np.matrix(a2i) # (1, 10).T @ (1, 26) -> (10, 26)
        delta1 += np.matrix(d2i[1:]).T @ np.matrix(a1i) # (1, 25).T @ (1, 401) -> (25, 401)

    delta1 = delta1 / m
    delta2 = delta2 / m

    return serialize(delta1, delta2)

def gradient_checking(theta, X, y, epsilon, regularized=False):
    def a_numeric_grad(plus, minus, epsilon, regularized=False):
        """calculate a partial gradient with respect to 1 theta"""
        if regularized:
            return (regularized_cost(plus, X, y) - regularized_cost(minus, X, y)) / (epsilon * 2)
        else:
            return (cost(plus, X, y) - cost(minus, X, y)) / (epsilon * 2)

    theta_matrix = expand_array(theta)  # expand to (10285, 10285)
    epsilon_matrix = np.identity(len(theta)) * epsilon

    plus_matrix = theta_matrix + epsilon_matrix
    minus_matrix = theta_matrix - epsilon_matrix

    # calculate numerical gradient with respect to all theta
    numeric_grad = np.array([a_numeric_grad(plus_matrix[i], minus_matrix[i], epsilon, regularized)
                                    for i in range(len(theta))])

    # analytical grad will depend on if you want it to be regularized or not
    analytic_grad = regularized_gradient(theta, X, y) if regularized else gradient(theta, X, y)

    # If you have a correct implementation, and assuming you used EPSILON = 0.0001
    # the diff below should be less than 1e-9
    # this is how original matlab code do gradient checking
    diff = np.linalg.norm(numeric_grad - analytic_grad) / np.linalg.norm(numeric_grad + analytic_grad)

    print('If your backpropagation implementation is correct,\nthe relative difference will be smaller than 10e-9 (assume epsilon=0.0001).\nRelative Difference: {}\n'.format(diff))

def expand_array(arr):
    # turn matrix back to ndarray
    return np.array(np.matrix(np.ones(arr.shape[0])).T @ np.matrix(arr))



######################################## RUN CODE ########################################
X_raw, y_raw = load_data('ex4data1.mat', transpose=False)
X = np.insert(X_raw, 0, np.ones(X_raw.shape[0]), axis=1)#增加全部为1的一列
y = expand_y(y_raw)
t1, t2 = load_weight('ex4weights.mat')

theta = serialize(t1, t2)
a1, z2, a2, z3, h = feed_forward(theta, X)
cost(theta, X, y)

d1, d2 = deserialize(gradient(theta, X, y))

gradient_checking(theta, X, y, epsilon= 0.0001)#这个运行很慢，谨慎运行