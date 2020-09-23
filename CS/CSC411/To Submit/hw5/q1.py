'''
Question 1 Skeleton Code

Here you should implement and evaluate the Conditional Gaussian classifier.
'''

import data
import numpy as np
# Import pyplot - plt.imshow is useful!
import matplotlib.pyplot as plt

def compute_mean_mles(train_data, train_labels):
    '''
    Compute the mean estimate for each digit class

    Should return a numpy array of size (10,64)
    The ith row will correspond to the mean estimate for digit class i
    '''
    means = np.zeros((10, 64))
    # create a dictionary to record num for each digit class
    d = {}
    for label in train_labels:
        if label not in d:
            d[label] = 1
        else:
            d[label] = d[label] + 1

    # Compute means
    for i in range(len(train_labels)):
        label = int(train_labels[i])
        means[label] += train_data[i]

    means = means/700 #based on the result of dictionary where 700 example for each labels
    return means


def compute_sigma_mles(train_data, train_labels):
    '''
    Compute the covariance estimate for each digit class

    Should return a three dimensional numpy array of shape (10, 64, 64)
    consisting of a covariance matrix for each digit class
    '''
    covariances = np.zeros((10, 64, 64))
    # Compute covariances
    means = compute_mean_mles(train_data, train_labels)

    # create a dictionary to record num for each digit class
    d = {}
    for label in train_labels:
        if label not in d:
            d[label] = 1
        else:
            d[label] = d[label] + 1

    # use the training example to fill the covariance matrix
    for i in range(len(train_data)):
        label = int(train_labels[i])
        term = (train_data[i] - means[label])[:,None]
        stuff = ( term @ term.T)
        covariances[label] += stuff

    # update convariance matrix by dividing len of each digit class
    # add 0.01I
    for i in range(10):
        covariances[i] = covariances[i]/d[i] + 0.01* np.identity(64)
    return covariances

def generative_likelihood(digits, means, covariances):
    '''
    Compute the generative log-likelihood:
        log p(x|y,mu,Sigma)

    Should return an n x 10 numpy array 
    '''
    # num of example
    num_example = len(digits)
    res = np.zeros((num_example, 10))

    for i in range(len(digits)):
        digit = digits[i]
        for k in range(10):
            mean = means[k]
            cov_matrix = covariances[k]
            part_1 = -32 * np.log(2*np.pi) - 0.5 * np.log(np.linalg.det(cov_matrix))
            part_2 = -0.5 * (np.transpose(digit - mean)@ np.linalg.inv(cov_matrix)@(digit - mean))
            log_likelihood = part_1 + part_2
            res[i,k] = log_likelihood
    return res


def conditional_likelihood(digits, means, covariances):
    '''
    Compute the conditional likelihood:

        log p(y|x, mu, Sigma)

    This should be a numpy array of shape (n, 10)
    Where n is the number of datapoints and 10 corresponds to each digit class
    '''
    num_example = len(digits)
    res = np.zeros((num_example, 10))

    # get matrix of log p(x|y,mu,Sigma)

    helper_matrix = generative_likelihood(digits, means, covariances)

    for i in range(num_example):
        sum_prob = np.sum(np.exp(helper_matrix[i])) #sum_k p(x|y,mu,Sigma)
        for k in range(10):
            inference = np.log(0.1) + helper_matrix[i,k] - np.log(sum_prob)
            res[i,k] = inference
    return res


def avg_conditional_likelihood(digits, labels, means, covariances):
    '''
    Compute the average conditional likelihood over the true class labels

        AVG( log p(y_i|x_i, mu, Sigma) )

    i.e. the average log likelihood that the model assigns to the correct class label
    '''
    cond_likelihood = conditional_likelihood(digits, means, covariances)
    sum = 0
    for i in range(len(labels)):
        label = int(labels[i])
        sum += cond_likelihood[i, label]

    # Compute as described above and return
    return sum/len(labels)

def classify_data(digits, means, covariances):
    '''
    Classify new points by taking the most likely posterior class
    '''
    cond_likelihood = conditional_likelihood(digits, means, covariances)
    # Compute and return the most likely class
    res = []
    for array in cond_likelihood:
        most_possible_class = array.argmax()
        res.append(most_possible_class)
    return res

def main():
    train_data, train_labels, test_data, test_labels = data.load_all_data('data')
    # Fit the model
    means = compute_mean_mles(train_data, train_labels)
    covariances = compute_sigma_mles(train_data, train_labels)

    # Evaluation
    train_avg_conditional_log_likelihood = avg_conditional_likelihood(train_data, train_labels, means, covariances)
    test_avg_conditional_log_likelihood = avg_conditional_likelihood(test_data, test_labels, means, covariances)
    print('The average conditional log-likehood for train set: {}'.format(train_avg_conditional_log_likelihood))
    print('The average conditional log-likehood for test set: {}'.format(test_avg_conditional_log_likelihood))

    train_set_predict = classify_data(train_data, means, covariances)
    test_set_predict = classify_data(test_data, means, covariances)

    train_set_accuracy = sum(train_set_predict == train_labels) / len(train_labels)
    test_set_accuracy = sum(test_set_predict == test_labels) / len(test_labels)

    print('The accuracy of train set prediction is {}'.format(train_set_accuracy))
    print('The accuracy of test set prediction is {}'.format(test_set_accuracy))

    # for each class, plot the leading eigenvector.
    k = 1
    for cov in covariances:
        eigenvalues, eigenvectors = np.linalg.eig(cov)
        leading_eigenvector = eigenvectors.T[0] #first column of eigenvector matrix
        #reshape
        leading_eigenvector = leading_eigenvector.reshape((8,8))
        plt.title("Class {}".format(str(k)))
        plt.set_cmap('gray')
        plt.imshow(leading_eigenvector)
        plt.show()
        k+=1


if __name__ == '__main__':
    main()
