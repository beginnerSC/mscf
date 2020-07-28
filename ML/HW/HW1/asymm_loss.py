from scipy.stats import norm
import numpy as np

#Set some parameters
beta = 0.5
b = 2
sigma = 2
a = 1

#Define the loss function, where z = y - yhat
def loss(z):
    return b*(np.exp(a*z)-a*z-1)

#Estimation functions
#Estimation using the conditional expectation of Y|X
def f_condexp(x):
    return beta*x

#TODO: Put your function in here.  You can reference a,b,sigma, and it will just pull them from
# the outside namespace
def f_yours(x):
    return ????????????

#Simulation to see how you do
reps = 1000

#Just generate the X variables normally.  We don't really care
x = norm.rvs(size=reps, loc=0, scale=1)

#Generate the Y variables from our normal model
y = norm.rvs(size=reps, loc=x*beta, scale=sigma)

#Calculate the fitted values for each method
yhat_condexp = np.apply_along_axis(f_condexp, 0, x)
yhat_yours = np.apply_along_axis(f_yours, 0, x)

#Compute the losses
condexp_losses = np.apply_along_axis(loss, 0, y-yhat_condexp)
your_losses = np.apply_along_axis(loss, 0, y-yhat_yours)

print("Average loss of the conditional expectation:",
      round(np.mean(condexp_losses),2))

print("Average loss of your method:", 
      round(np.mean(your_losses),2))

