import scipy

#You get to observe a bunch of data (that turns out to be worthless)
#Returns a data set with 100 variables and n data points
#The first 100 columns are the X variables (called X1,...X100)
#The last column is the response (called y)
def get_data(n):
    p=1000
    X = scipy.stats.norm().rvs(n*p).reshape((n,p))
    Y = scipy.stats.norm().rvs(n)
    return(X,Y)

#Generate some data
n = 100
X_train, y_train = get_data(n)
X_test, y_test = get_data(n)
train = get_data(n)
test = get_data(n)

