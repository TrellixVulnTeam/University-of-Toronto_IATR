# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 20:39:09 2017

"""
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston
np.random.seed(0)
from scipy.misc import logsumexp
from sklearn.model_selection import train_test_split

# load boston housing prices dataset
boston = load_boston()
x = boston['data']
N = x.shape[0]
x = np.concatenate((np.ones((506,1)),x),axis=1) #add constant one feature - no bias needed
d = x.shape[1]
y = boston['target']

idx = np.random.permutation(range(N))

#helper function
def l2(A,B):
    '''
    Input: A is a Nxd matrix
           B is a Mxd matirx
    Output: dist is a NxM matrix where dist[i,j] is the square norm between A[i,:] and B[j,:]
    i.e. dist[i,j] = ||A[i,:]-B[j,:]||^2
    '''
    A_norm = (A**2).sum(axis=1).reshape(A.shape[0],1)
    B_norm = (B**2).sum(axis=1).reshape(1,B.shape[0])
    dist = A_norm+B_norm-2*A.dot(B.transpose())
    return dist

 
"""
When we have a new test example x, based on its distance to each training set examples, we assign a(i).
Then, we have matrix A to get the w*.
Thus, we can get predicted y based on new x and w*.
"""
#to implement
def LRLS(test_datum, x_train, y_train, tau,lam=1e-5):
    '''
    Input: test_datum is a dx1 test vector
           x_train is the N_train x d design matrix
           y_train is the N_train x 1 targets vector
           tau is the local reweighting parameter
           lam is the regularization parameter
    output is y_hat the prediction on test_datum
    '''
    # calculate the distances between test_datum and each training set examples
    dist = l2(test_datum, x_train)

    # do transformation to dist
    dist = np.divide(-dist, 2*(tau**2))

    # get the max number B in dist
    B = np.max(dist)

    # create numerator array and denominator
    numerator_array = np.exp(dist - B)
    denominator = np.exp(logsumexp(dist - B))

    # diagonal numbers
    a = np.divide(numerator_array, denominator)[0]

    # create diagonal matrix A
    A = np.diag(a)

    # get w*

    # X^TAX + lamdaI
    matrix_1 = x_train.transpose()@A@x_train + lam*np.identity(d)

    # X^TAy
    matrix_2 = x_train.transpose()@A@y_train

    target_w = np.linalg.solve(matrix_1, matrix_2)

    predicted_y = test_datum @ target_w

    return predicted_y

def run_validation(x,y,taus,val_frac):
    '''
    Input: x is the N x d design matrix
           y is the N x 1 targets vector    
           taus is a vector of tau values to evaluate
           val_frac is the fraction of examples to use as validation data
    output is
           a vector of training losses, one for each tau value
           a vector of validation losses, one for each tau value
    '''
    training_loss = []
    validation_loss = []

    #split data set to train set and validation set
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = val_frac, random_state=0)

    for tau in taus:
        predicted_y_array = []
        for test_datum in X_test:
            predicted_y = LRLS(test_datum.reshape((1,d)), X_train, Y_train, tau, lam=1e-5)
            predicted_y_array.append(predicted_y)
        validation_cost = np.sum( (np.array(predicted_y) - Y_test)**2 ) / (2. * N * val_frac)
        train_cost = np.sum( (np.array(predicted_y) - Y_train)**2 ) / (2. * N * (1-val_frac))

        validation_loss.append(validation_cost)
        training_loss.append(train_cost)

    return np.array(training_loss), np.array(validation_loss)

if __name__ == "__main__":
    # In this excersice we fixed lambda (hard coded to 1e-5) and only set tau value. Feel free to play with lambda as well if you wish
    taus = np.logspace(1.0,3,200)
    train_losses, test_losses = run_validation(x,y,taus,val_frac=0.3)
    plt.semilogx(train_losses)
    plt.savefig('train_losses.jpg')

    plt.semilogx(test_losses)
    plt.savefig('validation_losses.jpg')

