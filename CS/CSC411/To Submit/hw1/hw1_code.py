from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplus
import random
import math
def load_data():
    data = []


    # read data from file
    real_file = open('clean_real.txt', 'r')
    for line in real_file:
        data.append((line.strip(), 1))


    fake_file = open('clean_fake.txt', 'r')
    for line in fake_file:
        data.append((line.strip(), 0))


    # shuffle the raw data
    random.shuffle(data)

    train_set_upper_bound = int(len(data) * 0.7)
    validation_set_upper_bound = int(len(data) * 0.85)

    x_input = [item[0] for item in data]
    label = [item[1] for item in data]
    train_set_headlines = x_input[:train_set_upper_bound]

    # vectorize input
    vectorizer = CountVectorizer()
    vector_input = vectorizer.fit_transform(x_input).toarray()

    train_set_input = vector_input[:train_set_upper_bound]
    train_set_label = label[:train_set_upper_bound]

    validation_set_input = vector_input[train_set_upper_bound:validation_set_upper_bound]
    validation_set_label = label[train_set_upper_bound:validation_set_upper_bound]

    test_set_input = vector_input[validation_set_upper_bound:]
    test_set_label = label[validation_set_upper_bound:]

    return train_set_headlines, train_set_input, train_set_label, validation_set_input, validation_set_label, test_set_input, test_set_label, vectorizer.get_feature_names()


def select_model(train_input, train_label, validation_input, validation_label):
    # model with Gini coefficient and max_depth from 2 to 10.
    for i in range(2, 11):
        model = tree.DecisionTreeClassifier(criterion='gini', max_depth=i)
        model.fit(train_input, train_label)
        prediction = model.predict(validation_input)
        prediction_res = [prediction[i] == validation_label[i] for i in range(len(prediction))]
        accuracy = sum(prediction_res) / len(prediction)

        print("For the model with Gini coefficient and the tree max depth " + str(i) + ", the validation accuracy is" + ' ' + str(accuracy))

    # model with information gain and max_depth from 2 to 10.
    for i in range(2, 11):
        model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=i)
        model.fit(train_input, train_label)
        prediction = model.predict(validation_input)
        prediction_res = [prediction[i] == validation_label[i] for i in range(len(prediction))]
        accuracy = sum(prediction_res) / len(prediction)

        print("For the model with Entropy coefficient and the tree max depth " + str(i) + ", the validation accuracy is" + ' ' + str(
            accuracy))

"""
Based on the input list of label, return the entropy.
"""
def compute_entropy(labels):
    num_one = sum(labels)
    num_zero = len(labels) - num_one
    if num_one == len(labels) or num_zero == len(labels):
        return 0
    p_one = num_one / len(labels)
    p_zero = num_zero / len(labels)
    entropy =  -p_one * math.log(p_one, 2) - p_zero * math.log(p_zero, 2)
    return entropy

def compute_information_gain(headlines, labels, keyword):
    with_keyword_headlines = []
    no_keyword_headlines = []

    with_keyword_labels = []
    no_keyword_labels = []
    for i in range(len(headlines)):
        lst = headlines[i].split()
        if keyword in lst:
            with_keyword_headlines.append(headlines[i])
            with_keyword_labels.append(labels[i])
        else:
            no_keyword_headlines.append(headlines[i])
            no_keyword_labels.append(labels[i])

    H_Y = compute_entropy(labels)
    H_left = (len(with_keyword_labels) / len(labels)) * compute_entropy(with_keyword_labels)
    H_right = (len(no_keyword_labels) / len(labels)) * compute_entropy(no_keyword_labels)
    res = H_Y - H_left - H_right
    return res

"""
Output decision tree with max-depth 10 and type Gini
"""
def plot(feature_names, train_input, train_label):
    # generate tree
    model = tree.DecisionTreeClassifier(criterion='gini', max_depth=10)
    model.fit(train_input, train_label)

    dot_data = StringIO()
    export_graphviz(model, out_file=dot_data,
                    filled=True, rounded=True,
                    special_characters=True, feature_names=feature_names, class_names=['fake', 'real'])

    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('tree plot.png')
    Image(graph.create_png())
    return model

if __name__ == '__main__':
    # pre-processing
    train_headlines, train_input, train_label, validation_input, validation_label, test_input, test_label, feature_cols = load_data()
    # validation test
    select_model(train_input, train_label, validation_input, validation_label)

    # plot the decision tree
    plot(feature_cols, train_input, train_label)

    # calculate entropy for different keywords
    keyword_lst = ['the', 'donald', 'trumps', 'hillary', 'le', 'market']
    for keyword in keyword_lst:
        I_G = compute_information_gain(train_headlines, train_label, keyword)
        print('When topmost splis is {}, information gain is {}'.format(keyword, I_G))
