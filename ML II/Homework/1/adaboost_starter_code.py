import numpy as np
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

#### These first 3 functions are free: you do not need to change them.

def find_split(X, y, wgts=None):
    """Find the best single split on one of the two variables, while incorporating weights.

    Inputs:
    X: a numpy array with 2 columns
    y: a numpy array with n elements
    wgts: a numpy array of n observation weights.

    Return two things:
    fit: The object returned by DecisionTreeClassifier
    tree_info: A dictionary with the following additional info. You don't need
    this, but it might help debug:

    variable_idx: Number of selected variable column
    threshold: Where that variable was split
    guess_less: which category is guessed if less than threshold
    guess_greater: which category is guessed if greater than threshold
    """

    n = X.shape[0]
    dtc = DecisionTreeClassifier(max_depth=1)
    fit = dtc.fit(X,y, sample_weight=wgts)
    tree_info = {
        'variable_idx' : fit.tree_.feature[0],
        'threshold' : fit.tree_.threshold[0],
        'guess_less' : np.argmax(fit.tree_.value[1])*2-1,
        'guess_greater' : np.argmax(fit.tree_.value[2])*2-1
    }

    return fit, tree_info


def draw_boosted_trees(trees, X, score=None):
    """Draw the data points and the decision boundaries used by the boosted trees.

    If score is supplied, the points are also shaded by the score.

    Inputs:
    trees: the list of tree objects output by my_adaboost
    X: a set of points output by get_circle_data (no y is needed)
    score: n-vector of scores to color each point (optional)
    Outputs: makes a plot.  You still need to call plt.show()
    """

    if score is not None:
        plt.scatter(X[:,0], X[:,1], c=score, cmap=plt.get_cmap('plasma'))
    else:
        plt.scatter(X[:,0], X[:,1])

    line_col='grey'

    for fit in trees:
        variable_idx = fit.tree_.feature[0]
        threshold = fit.tree_.threshold[0]

        if variable_idx == 0:
            plt.axvline(x=threshold, color=line_col)
        else:
            plt.axhline(y=threshold, color=line_col)


def get_circle_data(n):
    """Generate data for our example

    Inputs:
    n: number of samples

    Output: tuple with entries:
    X: an nx2 matrix of data points.
    y: class for the point (-1,1)
    """

    gaussian_2d = scipy.stats.multivariate_normal(mean = np.zeros(2), cov = np.eye(2))
    X = gaussian_2d.rvs(n)
    Y = np.where(X[:,0]**2 + X[:,1]**2 < 1, 1, -1)

    return X, Y

#### YOU DON'T NEED TO CHANGE FUNCTIONS ABOVE THIS LINE, THEY ARE FREE ####

#### You must finish the functions below this line ####

def my_adaboost(X, y, B=10):
    """Implement the adaboost function in my_adaboost

    Inputs:
    X, y: Data produced by get_circle_data()
    B: The number of trees to produce during boosting

    Returns:
    trees: a list of fitted tree objects
    alphas: a numpy array of B alpha values for the trees
    """

    n = X.shape[0]
    # Equal observation weights
    wgts = np.repeat(1/n, n)
    trees = [] # To store your trees.  Use append()
    alphas = np.zeros(B) # To store your alphas

    for b in range(B):
        # Find the next split, according to your current weights.
        # Hint: the returned tree supports predict()
        tree, info = find_split(X, y, wgts)

        # TODO: Fill in the rest of the body of this loop to implement
        # the AdaBoost algorithm from class

        # You can introduce whatever you need here.  At the very least,
        # it needs to result in updated wgts and
        # an additional entry in the trees list and the alphas vector.

        # TODO: You'll probably need some stuff here

        alphas[b] = # TODO: Add the new tree's weight
        trees.append() # TODO: Store the new tree
        wgts = # TODO: Update your observation weights

    return trees, alphas


def predict_ada(trees, alphas, X, y=None):
    """Calculate predictions for boosted trees from my_adaboost.

    If passed true y values, also computes *running* misclassification error
    across all B.

    Inputs:
    trees: list of trees returned by my_adaboost
    alphas: alpha vector returned by my_adaboost
    X: a data set to make predictions on
    y: the true labels for that data set, in {-1,1}.  If given, running prediction error is computed.

    Outputs: a list containing:
    score: the score for each point (before thresholding)
    preds: the thresholded scores: our guesses at class.
    test_err: a length B vector of misclassification error at each step (1 tree to B trees)
    """

    n = X.shape[0]
    B = len(trees)

    # Initialize a score vector to zero.
    # This will store the ongoing sum alpha_b fhat_b(x) for each point.
    score = np.zeros(n)

    # This will store the misclassification error at each step,
    # so we can see how it changes with the number of trees
    test_err = np.zeros(B)

    for b in range(B):
        # Update your score to include the contribution from tree b
        score = # TODO: Fill in the updated score
        preds = # TODO: Make predictions in {-1,1}

        if y is not None:
            # Record the misclassification error for the predictions
            # based on thresholding the current score
            test_err[b] = # TODO: Fill in the current misclassification error

    if y is None:
        return score, preds

    return score, preds, test_err

def calculate_partial_dependence_x1(trees, alphas, X):
    """Calculates the partial dependence plot over the first column of X.

    Fixes the first column at each point in the grid and evaluates the
    predictions at all of these fake points.  These predictions are used
    to obtain the partial dependence over x1.

    Inputs:
    trees: list of trees returned by my_adaboost
    alphas: list of alphas returned by my_adaboost
    X: data set to use for computing partial dependence.
    """

    m = 50 # Number of grid points to evaluate partial dependence
    x = np.linspace(np.min(X[:,0]), np.max(X[:,0]), m)

    # Somewhere to store the partial dependence values
    pdep = np.zeros(m)

    # We will fake a dataset and change its x1 values to match each evaluation points
    fake = X.copy()
    for i in range(m):
        fake[:,0] = x[i]
        # TODO: Fill in the actual calculation of the partial
        # dependence at x[i] below
        # HINT: Evaluate predict_ada on the fake data set and use
        # resulting predictions
        pdep[i] = # TODO

    return x, pdep
