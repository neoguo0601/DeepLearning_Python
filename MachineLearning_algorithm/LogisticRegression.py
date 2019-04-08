import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import matplotlib
import scipy.optimize as opt
from sklearn.metrics import classification_report #这个包是评价报告

def load_data(path, transposr=True):
    data = sio.loadmat(path)
    y = data.get('y')
    y = y.reshape(y.shape[0])

    X = data.get('X')

    if transposr:
        # for this dataset, you need a transpose to get the orientation right
        X = np.array([im.reshape((20, 20)).T for im in X])

        # and I flat the image again to preserve the vector presentation
        X = np.array([im.reshape(400) for im in X])

    return X, y

def plot_an_image(image):
    fig, ax = plt.subplots(figsize=(1,1))
    ax.matshow(image.reshape((20,20)), cmap = matplotlib.cm.binary)
    plt.xticks(np.array([]))  # just get rid of ticks
    plt.yticks(np.array([]))

def plot_100_image(X):
    size = int(np.sqrt(X.shape[1]))

    # sample 100 image, reshape, reorg it
    sample_idx = np.random.choice(np.arange(X.shape[0]), 100)  # 100*400
    sample_images = X[sample_idx, :]

    fig, ax_array = plt.subplots(nrows=10, ncols=10, sharey=True, sharex=True, figsize=(10, 10))

    for r in range(10):
        for c in range(10):
            ax_array[r, c].matshow(sample_images[10 * r + c].reshape((size, size)),
                                   cmap=matplotlib.cm.binary)
            plt.xticks(np.array([]))
            plt.yticks(np.array([]))  

def sigmoid(z):
    return 1/(1+np.exp(-z))
     
def gradient(theta, X, y):
    return (1 / len(X)) * X.T @ (sigmoid(X @ theta) - y)

def cost(theta, X, y):
    return np.mean(-y * np.log(sigmoid(X@theta)) - (1-y) * np.log(1-sigmoid(X@theta)))

def regularized_cost(theta, X, y, l=1):
    theta_j1_to_n = theta[1:]
    regularized_term = (1/(2*len(X)))*np.power(theta_j1_to_n, 2).sum()
    return cost(theta, X, y) + regularized_term

def regularized_gradient(theta, X, y, l=1):
    theta_j1_to_n = theta[1:]
    regularized_theta = (1/len(X)) * theta_j1_to_n
    regularized_term = np.concatenate((np.array([0]), regularized_theta))
    return gradient(theta, X, y) + regularized_term

def logistic_regression(X, y, l=1):
    theta = np.zeros(X.shape[1])
    res = opt.minimize(fun=regularized_cost,
                       x0=theta,
                       args=(X, y, l),
                       method='TNC',
                       jac=regularized_gradient,
                       options={'disp': True})
    final_theta = res.x        
    return final_theta

def predict(x, theta):
    prob = sigmoid(x @ theta)
    return (prob >= 0.5).astype(int)

################################## RUN CODE ############################### 
X, y = load_data('ex3data1.mat')

#print(X.shape)
#print(y.shape)

#pick_one = np.random.randint(0,5000)
#plot_an_image(X[pick_one,:])
#plt.show()
#print("this should be {}".format(y[pick_one]))

#plot_100_image(X)
#plt.show()

raw_X, raw_y = load_data('ex3data1.mat')
X = np.insert(raw_X, 0, values=np.ones(raw_X.shape[0]), axis=1)#插入了第一列（全部为1）
print(X.shape)

y_matrix = []

for k in range(1, 11):
    y_matrix.append((raw_y == k).astype(int))

# last one is k==10, it's digit 0, bring it to the first position，最后一列k=10，都是0，把最后一列放到第一列
y_matrix = [y_matrix[-1]] + y_matrix[:-1]
y = np.array(y_matrix)

t0 = logistic_regression(X, y[0])
print(t0.shape)
y_pred = predict(X, t0)
print('Accuracy={}'.format(np.mean(y[0] == y_pred)))    