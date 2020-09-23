import numpy as np
import pandas as pd

def sel(L):
    res = [ (num**2)/2 for num in L]
    return res


def hl(L, hyperparameter):
    res = []
    for num in L:
        abs_num = abs(num)
        if abs_num < hyperparameter:
            res.append((num**2)/2)
        else:
            res.append(hyperparameter*(abs_num - hyperparameter/2))
    return res


"""
To calculate H'_delta(y-t)
"""
def helper(a, delta):
    if abs(a) <= delta:
        return a
    elif a > delta:
        return delta
    else:
        return -delta


"""
Returns the value of the parameters w and b after performing (full batch mode) gradient descent 
to minimize this model’s cost function for num_iter iterations.
"""
def gradient_descent(X, y, lr, num_iter, delta):
    # get the # of training example and # of dimension of x
    n = X.shape[0]
    d = X.shape[1]

    # initialize vector w and vector b
    w = np.zeros(d)
    b = 0

    for i in range(num_iter):
        predicted_value = X@w + b

        # get the residual
        a = predicted_value - y

        # store the residual vector to pandas dataframe
        df = pd.DataFrame({'residual': a})

        #according to value of a, calculate the H'_delta(a) and store the corresponding vertor to dataframe
        df['derivative'] = df.apply(lambda row: helper(row['residual'], delta), axis=1 )

        # extract the derivative vector from dataframe
        derivative = np.array(df['derivative'])

        # update w and b
        w = w - X.transpose()@derivative * (lr/n)
        b = b - np.mean(derivative)*lr

    return w, b




if __name__ == '__main__':
    # y = list(range(-999,999))
    # sel_res = sel(y)
    # hl_res = hl(y, 333)
    # df = pd.DataFrame({'y':y, 'sel_res':sel_res, 'hl_res': hl_res})
    # df.to_excel("Q1_a.xlsx", sheet_name='Sheet_name_1')
    X = np.array([[10,5,4],[6,7,4],[9,3,2]])
    y = np.array([100,90,80])
    lr = 0.05
    num_iter = 50
    delta = 5
    gradient_descent(X, y, lr, num_iter, delta)
