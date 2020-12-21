def get_data(n):
  x = np.random.uniform(size=n)
  y = x**2-x/2.0 + np.random.normal(size=n,scale=0.1)
  idx = np.argsort(x)
  return(x[idx].reshape((-1,1)),y[idx].reshape((-1,1)))

def true_mean(x):
  return(x**2-x/2.0)
